# Python Health Monitor

[![CI](https://github.com/rdaneel-ali/python-health-monitor/actions/workflows/ci.yaml/badge.svg)](https://github.com/rdaneel-ali/python-health-monitor/actions/workflows/ci.yaml)
[![License: GPL v2](https://img.shields.io/badge/License-GPL%20v2-blue.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-brightgreen)]()

A robust health monitoring tool for reliable endpoint monitoring with enterprise-grade features and planned cloud integration capabilities.

## Overview

This tool provides comprehensive health monitoring for web endpoints with built-in resilience patterns, structured logging, and extensible architecture. Built with production reliability in mind while maintaining simplicity for quick deployment scenarios.

## Features

### Core Monitoring
- **Multi-endpoint health checking** with configurable parameters
- **Resilient request handling** with retry logic and exponential backoff  
- **Structured logging** for operational visibility and debugging
- **Flexible configuration** via YAML/JSON with environment variable overrides

### Architecture & Quality
- **Modular design** with clean separation of concerns
- **Comprehensive test coverage** using pytest
- **CLI and programmatic interfaces** for versatile integration
- **Production-ready packaging** with proper dependency management

### Planned Cloud Integration
- **AWS Lambda deployment** for serverless operation
- **CloudWatch integration** for centralized logging and alerting
- **CI/CD pipeline** with automated testing and deployment

### Prerequisites
- Python 3.8+
- `pip` installed (comes with Python)

---


### Installation

Clone and install in editable mode:

```bash
# Clone repository
git clone https://github.com/rdaneel-ali/python-health-monitor.git
cd python-health-monitor

# Install the project and its dependencies
# The `-e` flag installs in editable mode for development
pip install -e .
```

Alternatively install directly from GitHub without cloning

```bash
# Install the latest version from the main branch
pip install git+https://github.com/rdaneel-ali/python-health-monitor.git

# Or install a specific release/tag
pip install git+https://github.com/rdaneel-ali/python-health-monitor.git@v0.1.0
```

### Quick Start 🚀
The project includes a **default configuration** (`config/config.yaml`) so you can run it immediately after installation.

```bash
# Run the monitor with the included default config
python-health-monitor
```
**Example Output:**
```bash
Loaded configuration from config/config.yaml
Logging configured: logs/health_monitor.log at INFO level
Starting health checks...
Dummy API: ✅ SUCCESS - Success: 200

Health check summary: 1/1 endpoints healthy
🎉 All endpoints are healthy!
Health checks completed
```
**Custom Configuration file**
To run with your own configuration, provide a file via `--config`:
```bash
python-health-monitor --config /path/to/my/config.yaml
```
### Dependencies

**Core Application:**
- `requests` - HTTP client for health checks
- `PyYAML` - Configuration file parsing

**Testing & Quality:**
- `pytest` - Testing framework

**AWS & LocalStack Integration:**
- `boto3` - AWS SDK for Python
- `awscli-local` - LocalStack-compatible AWS CLI wrapper
- `localstack-client` - LocalStack service management

> All AWS-related dependencies work seamlessly with LocalStack for local development

### Basic Usage

```bash
# Run with the default configuration
python-health-monitor

# Run with a custom configuration file
python-health-monitor --config /path/to/my/config.yaml

# Show help for command-line options
python-health-monitor --help
```

### Configuration ⚙️
The monitor is **configuration-driven**, so you can adjust behavior without modifying code.

**Default Configuration**
The tool loads `config/config.yaml` by default

```yaml
# config/config.yaml
# A simple, single-source-of-truth configuration file.
monitor:
  timeout: 5        # Request timeout in seconds
  retries: 3        # Number of retry attempts

logging:
  file: "logs/health_monitor.log"
  level: "INFO"

endpoints:
  - name: "Python.org"
    url: "https://python.org"
  - name: "Example Site"
    url: "https://example.com"
  - name: "Google"
    url: "https://google.com"
```
This file is ready to use immediately — no changes required.

**Custom Configuration**
You can create your own YAML or JSON file and pass it with `--config`:

```bash
python-health-monitor --config /path/to/my/config.yaml
```

Example custom file:
```yaml
monitor:
  timeout: 10
  retries: 5

logging:
  file: "logs/prod_monitor.log"
  level: "WARNING"

endpoints:
  - name: "Production API"
    url: "https://api.example.com/health"
  - name: "Docs"
    url: "https://docs.example.com"
```

### Environment Overrides
Environment variables override config file values (useful in CI/CD or Docker)

```bash
export MONITOR_TIMEOUT=15
export MONITOR_RETRIES=2
python-health-monitor
```


### Working Example ✅
Here's how to verify the monitor works in your system:

- **1. Clone & install**

```bash
git clone https://github.com/rdaneel-ali/python-health-monitor.git
cd python-health-monitor
pip install -e .
```

- **2. Run with default config**

  ```bash
  python-health-monitor
  ```

  Example output

  ```bash
  [INFO] Checking endpoint: Python.org (https://python.org)
  [INFO] Endpoint 'Python.org' is healthy (200)
  [INFO] Checking endpoint: Example Site (https://example.com)
  [INFO] Endpoint 'Example Site' is healthy (200)
  [INFO] Checking endpoint: Google (https://google.com)
  [INFO] Endpoint 'Google' is healthy (200)
  ```
  Logs are also written to `logs/health_monitor.log`.

- **3. Create a custom config**

  Save as `config/custom.yaml`:

  ```yaml
  monitor:
    timeout: 3
    retries: 2

  logging:
    file: "logs/custom_monitor.log"
    level: "DEBUG"

  endpoints:
    - name: "Google"
      url: "https://google.com"
    - name: "Broken API"
      url: "https://httpbin.org/status/500"
  ```

- **4. Run with custom config**

  ```bash 
    python-health-monitor --config config/custom.yaml
  ```

  Example output:

  ```bash
    [INFO] Checking endpoint: Google (https://www.google.com)
    [INFO] Endpoint 'Google' is healthy (200)
    [WARNING] Endpoint 'Broken API' returned status 500
  ```

## Architecture

### Design Principles

**Configuration-Driven Design**
- Externalized settings in YAML for flexibility without code changes
- Environment-specific configs (development, staging, production)

**Resilience Patterns**
- Retry logic with configurable attempts and delays
- Timeout handling to prevent hanging requests
- Graceful degradation when endpoints fail

**Observability**
- Structured logging with multiple severity levels
- File and console output for different use cases
- Detailed error messages for troubleshooting

**Modularity**
- Single-responsibility functions for testability
- Clear separation between configuration, execution, and reporting
- Type hints for code clarity and IDE support

### Error Handling Strategy

The script handles network failures gracefully:
- **Timeout errors**: Server too slow to respond
- **Connection errors**: DNS/network issues
- **HTTP errors**: Unexpected status codes
- **Configuration errors**: Missing/invalid YAML files

Each error type is logged with specific context for debugging.

## Development

### IDE Setup

This project includes VS Code configuration for streamlined development:

```json
// .vscode/launch.json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: Local Debug",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal",
      "justMyCode": true,
      "env": {
        "AWS_ACCESS_KEY_ID": "test",
        "AWS_SECRET_ACCESS_KEY": "test",
        "AWS_DEFAULT_REGION": "us-east-1",
        "LOCALSTACK_HOST": "localhost",
        "EDGE_PORT": "4566"
      }
    }
  ]
}
```

**Features:**
- Pre-configured LocalStack environment variables
- Debug support with breakpoints
- Integrated terminal output
- One-click debugging for any Python file

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=monitor tests/

# Run specific test files
pytest tests/test_monitor.py
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 monitor.py tests/

# Type checking (if using type hints)
mypy monitor.py
```

## Project Structure

```
python-health-monitor/
├── src/                                # Source code for the package
│   └── python_health_monitor/
│       ├── __init__.py                 # Makes 'python_health_monitor' a Python package
│       └── monitor.py                  # The core health monitoring script
│
├── tests/                              # Unit test suite
│   ├── __init__.py                     # Makes the 'tests' directory a package
│   ├── test_monitor.py                 # Tests for the core script logic
│   └── test_config.py                  # Tests for the configuration loading logic
│
├── config/                             # Directory for configuration files
│   └── config.yaml                     # The default configuration file
│
├── logs/                               # Log files are saved here
│   └── .gitkeep                        # Ensures this empty directory is tracked by Git
│
├── .gitignore                          # Specifies files and directories to be ignored by Git
├── pyproject.toml                      # The modern standard for Python project metadata
├── README.md                           # The project overview and documentation
└── LICENSE                             # Full text of the project's license
```

## Usage Examples

### Programmatic Usage

```python
# The import must now come from the installed package
from python_health_monitor.monitor import main

# To run the monitor with the default configuration, call main()
# It will load 'config.yaml' from your project root.
main()

# To run with a specific configuration file, pass the arguments as a list.
main(args=["--config", "config/production.yaml"])
```

### Command Line Options

```bash
# Run with the default configuration
python-health-monitor

# Use a custom configuration file
python-health-monitor --config /path/to/my/config.yaml

# Show help for command-line options
python-health-monitor --help
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Make your changes with tests
4. Run the test suite (`pytest`)
5. Commit your changes (`git commit -m 'Add new feature'`)
6. Push to your branch (`git push origin feature/new-feature`)
7. Create a Pull Request

### Development Guidelines
- Maintain test coverage above 85%
- Follow PEP 8 style guidelines
- Add docstrings for public functions
- Update documentation for new features
- Test both success and failure scenarios

## Deployment

### Production Deployment
```bash
# Install the project and its production dependencies
pip install .

# Set up configuration
cp config/config.yaml config/production.yaml
# Edit production.yaml with your endpoints

# Run with production config
python -m python_health_monitor.monitor --config config/production.yaml
```

### Systemd Service (Linux)
Create `/etc/systemd/system/health-monitor.service`:

```ini
[Unit]
Description=Health Monitor Service
After=network.target

[Service]
Type=simple
User=monitor
WorkingDirectory=/path/to/python-health-monitor
ExecStart=/usr/bin/python3 monitor.py --config config/production.yaml
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

## Roadmap

- [ ] **Phase 1**: Enhanced reporting and alerting
  - [ ] Email notifications
  - [ ] Slack/Teams webhook integration
  - [ ] HTML report generation
  - [ ] Secure credential management (.env files, AWS Secrets Manager)
- [ ] **Phase 2**: Cloud integration
  - [ ] LocalStack development environment setup
  - [ ] AWS Lambda function development and testing
  - [ ] CloudWatch metrics and alarms (LocalStack)
  - [ ] Production AWS deployment automation
  - [ ] S3 report storage
- [ ] **Phase 3**: Advanced features
  - [ ] Docker containerization
  - [ ] Prometheus metrics export
  - [ ] Web dashboard interface

## License

Licensed under the GNU General Public License v2.0 (GPLv2) - see [LICENSE](LICENSE) file for details.

---

**Have questions or ideas?** Feel free to open an issue or start a discussion!
