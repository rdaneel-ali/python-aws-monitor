#!/usr/bin/env python3
"""
Health Monitor - A robust endpoint monitoring tool

Monitor web endpoints for availability with configurable retries,
structured logging, and YAML configuration.
"""

import argparse
import logging
import time
import yaml
import requests
from pathlib import Path
from typing import Dict, List, Tuple


def setup_logging(log_file: str = "logs/health_monitor.log", log_level: str = "INFO") -> None:
    """Configure structured logging to file and console."""
    # Create logs directory if it doesn't exist
    Path(log_file).parent.mkdir(parents=True, exist_ok=True)
    
    logging.basicConfig(
        level=getattr(logging, log_level.upper()),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )


def load_config(config_path: str) -> Dict:
    """Load YAML configuration file with error handling."""
    logger = logging.getLogger(__name__)
    
    try:
        config_file = Path(config_path)
        if not config_file.exists():
            logger.error(f"Configuration file not found: {config_path}")
            return {}
            
        with open(config_file, 'r') as f:
            config = yaml.safe_load(f)
            logger.info(f"Loaded configuration from {config_path}")
            return config
            
    except yaml.YAMLError as e:
        logger.error(f"Invalid YAML in config file: {e}")
        return {}
    except Exception as e:
        logger.error(f"Error loading configuration: {e}")
        return {}


def check_endpoint(endpoint: Dict, timeout: int = 5, retries: int = 3, delay: int = 2) -> Tuple[bool, str]:
    """
    Check single endpoint health with retries.
    
    Args:
        endpoint: Dict with 'url', 'name', 'expected_status' keys
        timeout: Request timeout in seconds
        retries: Maximum retry attempts
        delay: Seconds between retries
        
    Returns:
        Tuple of (success: bool, message: str)
    """
    logger = logging.getLogger(__name__)
    
    url = endpoint.get('url')
    name = endpoint.get('name', url)
    expected_status = endpoint.get('expected_status', 200)
    
    logger.info(f"Starting health check for {name} ({url})")
    
    for attempt in range(1, retries + 1):
        try:
            response = requests.get(url, timeout=timeout)
            
            if response.status_code == expected_status:
                logger.info(f"✅ {name} - SUCCESS ({response.status_code}) on attempt {attempt}")
                return True, f"Success: {response.status_code}"
            else:
                logger.warning(f"⚠️  {name} - Unexpected status {response.status_code} (expected {expected_status}) - attempt {attempt}/{retries}")
                
        except requests.exceptions.Timeout:
            logger.error(f"❌ {name} - Timeout after {timeout}s - attempt {attempt}/{retries}")
        except requests.exceptions.ConnectionError:
            logger.error(f"❌ {name} - Connection error - attempt {attempt}/{retries}")
        except requests.exceptions.RequestException as e:
            logger.error(f"❌ {name} - Request failed: {str(e)} - attempt {attempt}/{retries}")
        except Exception as e:
            logger.error(f"❌ {name} - Unexpected error: {str(e)} - attempt {attempt}/{retries}")
        
        # Wait before retry (except on last attempt)
        if attempt < retries:
            logger.info(f"Waiting {delay}s before retry...")
            time.sleep(delay)
    
    logger.error(f"🚫 {name} - FAILED after {retries} attempts")
    return False, f"Failed after {retries} attempts"


def run_health_checks(config: Dict) -> None:
    """Execute health checks for all configured endpoints."""
    logger = logging.getLogger(__name__)
    
    monitor_config = config.get('monitor', {})
    endpoints = config.get('endpoints', [])
    
    if not endpoints:
        logger.error("No endpoints configured for monitoring")
        return
    
    # Extract settings with defaults
    timeout = monitor_config.get('timeout', 5)
    retries = monitor_config.get('retries', 3)
    delay = monitor_config.get('delay', 2)
    
    logger.info(f"Starting health checks for {len(endpoints)} endpoints")
    logger.info(f"Configuration: timeout={timeout}s, retries={retries}, delay={delay}s")
    
    results = []
    
    # Check each endpoint
    for endpoint in endpoints:
        success, message = check_endpoint(endpoint, timeout, retries, delay)
        results.append({
            'name': endpoint.get('name', endpoint.get('url')),
            'url': endpoint.get('url'),
            'success': success,
            'message': message
        })
    
    # Generate summary report
    successful = sum(1 for r in results if r['success'])
    total = len(results)
    
    logger.info(f"Health check summary: {successful}/{total} endpoints healthy")
    
    if successful == total:
        logger.info("🎉 All endpoints are healthy!")
    else:
        failed = [r for r in results if not r['success']]
        logger.warning(f"⚠️  {len(failed)} endpoints failed:")
        for result in failed:
            logger.warning(f"  - {result['name']}: {result['message']}")


def main():
    """Main application entry point."""
    # Use script-relative path for config file
    script_dir = Path(__file__).parent
    default_config_path = script_dir / "config" / "config.yaml"
    
    parser = argparse.ArgumentParser(
        description="Health Monitor - Check endpoint availability with structured logging"
    )
    parser.add_argument(
        '--config', 
        default=str(default_config_path),
        help=f'Path to YAML configuration file (default: {default_config_path})'
    )
    
    args = parser.parse_args()
    
    # Load configuration
    config = load_config(args.config)
    if not config:
        print("ERROR: Could not load configuration. Exiting.")
        return 1
    
    # Setup logging from config
    monitor_config = config.get('monitor', {})
    log_file = monitor_config.get('log_file', 'logs/health_monitor.log')
    log_level = monitor_config.get('log_level', 'INFO')
    
    setup_logging(log_file, log_level)
    logger = logging.getLogger(__name__)
    
    logger.info("Health Monitor starting...")
    
    try:
        run_health_checks(config)
        logger.info("Health Monitor completed successfully")
        return 0
        
    except KeyboardInterrupt:
        logger.info("Health Monitor interrupted by user")
        return 0
    except Exception as e:
        logger.error(f"Health Monitor failed with error: {e}")
        return 1


if __name__ == "__main__":
    exit(main())