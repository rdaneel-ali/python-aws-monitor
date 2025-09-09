#!/usr/bin/env python3
"""
monitor.py

Python Health Monitor - Check endpoint availability and log results.

Author: Ali Awan
License: GNU General Public License v2 (GPLv2)
"""

import requests
import yaml
import logging
import argparse
import time
from pathlib import Path
from copy import deepcopy

# --------------------------------------------------------------------
# Paths & Defaults
# --------------------------------------------------------------------
def find_project_root():
    """Finds the project root by searching for pyproject.toml."""
    current_dir = Path(__file__).resolve().parent
    for parent in current_dir.parents:
        if (parent / "pyproject.toml").exists():
            return parent
    return current_dir

PROJECT_ROOT = find_project_root()
DEFAULT_CONFIG_PATH = PROJECT_ROOT / "config" / "config.yaml"
FALLBACK_LOG_FILE = PROJECT_ROOT / "logs" / "health_monitor.log"

# --------------------------------------------------------------------
# Configuration
# --------------------------------------------------------------------
def load_yaml(path: Path) -> dict:
    """Load a YAML file safely."""
    try:
        with open(path, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        print(f"WARNING: Config file not found: {path}")
        return {}
    except yaml.YAMLError as e:
        print(f"ERROR: Invalid YAML in {path}: {e}")
        return {}
    except Exception as e:
        print(f"ERROR: Failed to load config {path}: {e}")
        return {}

def load_config(config_file: str | None) -> dict:
    """Load YAML configuration from a specified or default path."""
    path = Path(config_file) if config_file else DEFAULT_CONFIG_PATH
    
    # Check if a specific file was provided but doesn't exist
    if config_file and not path.is_file():
        print(f"ERROR: Specified config file not found: {path}")
        return {}

    # Load from the determined path
    config = load_yaml(path)
    
    # If a config was loaded and it's not empty, print and return it
    if config:
        print(f"Loaded configuration from {path}")
        return config
    
    # Use a fallback if the default config is not found or is empty
    if path == DEFAULT_CONFIG_PATH:
        print("INFO: Using a fallback configuration.")
        # You can add a default, hardcoded config here if needed.
        # This prevents the script from crashing if no config.yaml exists.
        return {
            'logging': {'file': str(FALLBACK_LOG_FILE), 'level': 'INFO'},
            'monitor': {'timeout': 5, 'retries': 3, 'delay': 2},
            'endpoints': []
        }
    # Otherwise, no config was found and there's no fallback. Return an empty dict.
    return {}

def setup_logging(log_file: str, level: str = "INFO"):
    """Setup basic logging to file."""
    try:
        # Create logs directory if it doesn't exist
        Path(log_file).parent.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            filename=log_file,
            level=getattr(logging, level.upper(), logging.INFO),
            format="%(asctime)s [%(levelname)s] %(message)s",
        )
        print(f"Logging configured: {log_file} at {level} level")
    except Exception as e:
        print(f"ERROR: Could not setup logging: {e}")


def check_url(url, name, timeout=5, retries=3, delay=2):
    """Check URL health with retries and detailed logging."""
    print(f"Starting health check for {name} ({url})")
    logging.info(f"Starting health check for {name} ({url})")
    
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout)
            
            if response.status_code == 200:
                logging.info(f"✅ {name} - SUCCESS ({response.status_code}) on attempt {attempt}")
                return True, f"Success: {response.status_code}"
            else:
                logging.warning(f"⚠️  {name} - Unexpected status {response.status_code} - attempt {attempt}/{retries}")
                
        except requests.exceptions.Timeout:
            logging.error(f"❌ {name} - Timeout after {timeout}s - attempt {attempt}/{retries}")
        except requests.exceptions.ConnectionError:
            logging.error(f"❌ {name} - Connection error - attempt {attempt}/{retries}")
        except requests.exceptions.RequestException as e:
            logging.error(f"❌ {name} - Request failed: {str(e)} - attempt {attempt}/{retries}")
        except Exception as e:
            logging.error(f"❌ {name} - Unexpected error: {str(e)} - attempt {attempt}/{retries}")
        
        # Wait before retry (except on last attempt)
        if attempt < retries:
            logging.info(f"Waiting {delay}s before retry...")
            time.sleep(delay)
    
    logging.error(f"🚫 {name} - FAILED after {retries} attempts")
    return False, f"🚫Failed after {retries} attempts"


def main(args=None):
    parser = argparse.ArgumentParser(description="Python Health Monitor")
    # Argument for config file, default is handled inside load_config
    parser.add_argument("--config", help="Path to a custom config file")
    parsed_args = parser.parse_args(args)
        
    # Load configuration
    config = load_config(parsed_args.config)
    if not config:
        exit(1)
    
    # Setup logging
    try:
        # Resolve log file path relative to APP_DIR if it's a relative path
        log_file = config['logging']['file']
        full_log_path = PROJECT_ROOT  / log_file if not Path(log_file).is_absolute() else Path(log_file)
        
        log_level = config['logging']['level']
        setup_logging(str(full_log_path), log_level)
    except KeyError as e:
        print(f"ERROR: Missing logging configuration key: {e}")
        exit(1)
    except Exception as e:
        print(f"ERROR: Failed to setup logging: {e}")
        exit(1)

    
    # Get monitor settings
    try:
        monitor_config = config.get("monitor", {})
        timeout = monitor_config.get("timeout", 5)
        retries = monitor_config.get("retries", 3)
        delay = monitor_config.get("delay", 2)
        endpoints = config.get("endpoints", [])
    except Exception as e:
        error_msg = f"Failed to parse monitor configuration: {e}"
        print(f"ERROR: {error_msg}")
        logging.error(error_msg)
        exit(1)
    
    if not endpoints:
        print("ERROR: No endpoints configured for monitoring")
        logging.error("No endpoints configured for monitoring")
        exit(1)            
    
    print("Starting health checks...")
    logging.info("Health Monitor starting...")
    logging.info(f"Configuration: timeout={timeout}s, retries={retries}, delay={delay}s")
    logging.info(f"Starting health checks for {len(endpoints)} endpoints")
    
    results = []
    
    # Check each endpoint
    for endpoint in endpoints:
        try:
            url = endpoint["url"]
            name = endpoint.get("name", url)
            
            ok, info = check_url(url, name, timeout, retries, delay)
            
            # Store results
            results.append({
                'name': name,
                'url': url,
                'success': ok,
                'message': info
            })
            
            # Print results
            status = "✅ SUCCESS" if ok else "FAILED"
            print(f"{name}: {status} - {info}")
            
        except KeyError as e:
            error_msg = f"Missing required field in endpoint config: {e}"
            print(f"ERROR: {error_msg}")
            logging.error(error_msg)
        except Exception as e:
            error_msg = f"Error processing endpoint {endpoint}: {e}"
            print(f"ERROR: {error_msg}")
            logging.error(error_msg)
    
    # Generate summary report
    try:
        successful = sum(1 for r in results if r['success'])
        total = len(results)
        
        print(f"\nHealth check summary: {successful}/{total} endpoints healthy")
        logging.info(f"Health check summary: {successful}/{total} endpoints healthy")
        
        if successful == total:
            print("🎉 All endpoints are healthy!")
            logging.info("🎉 All endpoints are healthy!")
        else:
            failed = [r for r in results if not r['success']]
            print(f"⚠️  {len(failed)} endpoints failed:")
            logging.warning(f"⚠️  {len(failed)} endpoints failed:")
            for result in failed:
                print(f"  - {result['name']}: {result['message']}")
                logging.warning(f"  - {result['name']}: {result['message']}")
                
    except Exception as e:
        print(f"ERROR: Failed to generate summary: {e}")
        logging.error(f"Failed to generate summary: {e}")
    
    print("Health checks completed")
    logging.info("Health Monitor completed")


if __name__ == "__main__":
    main()