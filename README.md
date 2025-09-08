# Python Health Monitor

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

## Quick Start

### Prerequisites
- Python 3.8+

### Installation

```bash
# Clone repository
git clone https://github.com/yourusername/python-health-monitor.git
cd python-health-monitor

# Install dependencies
pip install -r requirements.txt

# Optional: Install in development mode
pip install -e .
```

### Basic Usage

```bash
# Run with default configuration
python monitor.py

# Use custom configuration
python monitor.py --config config/production.yaml

# Show help
python monitor.py --help
```

### Configuration

Create a configuration file (YAML or JSON):

```yaml
# config/monitor.yaml
endpoints:
  - name: "Production API"
    url: "https://api.example.com/health"
    timeout: 10
    retries: 3
    expected_status: 200
  - name: "Documentation Site"
    url: "https://docs.example.com"
    timeout: 5
    retries: 2

logging:
  level: "INFO"
  format: "structured"
  file: "logs/monitor.log"

monitoring:
  interval: 60
  alert_threshold: 3
  parallel_checks: true
```

## Development

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
├── monitor.py          # Main monitoring script
├── config/            # Configuration files
│   ├── default.yaml
│   └── production.yaml
├── tests/             # Test suite
│   ├── test_monitor.py
│   └── test_config.py
├── logs/              # Log files
├── requirements.txt   # Dependencies
└── README.md
```

## Usage Examples

### Programmatic Usage

```python
from monitor import HealthMonitor

# Initialize with configuration
monitor = HealthMonitor(config_file='config/production.yaml')

# Run single check
results = monitor.check_all()

# Run continuous monitoring
monitor.start_monitoring(interval=60)
```

### Command Line Options

```bash
# Basic monitoring
python monitor.py

# Custom configuration
python monitor.py --config config/staging.yaml

# One-time check (no continuous monitoring)
python monitor.py --once

# Verbose output
python monitor.py --verbose

# Output to specific log file
python monitor.py --log-file /path/to/monitor.log
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
# Install production dependencies
pip install -r requirements.txt

# Set up configuration
cp config/default.yaml config/production.yaml
# Edit production.yaml with your endpoints

# Run with production config
python monitor.py --config config/production.yaml
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
- [ ] **Phase 2**: Cloud integration
  - [ ] AWS Lambda serverless deployment
  - [ ] CloudWatch metrics and alarms
  - [ ] S3 report storage
- [ ] **Phase 3**: Advanced features
  - [ ] Docker containerization
  - [ ] Prometheus metrics export
  - [ ] Web dashboard interface

## License

Licensed under the GNU General Public License v2.0 (GPLv2) - see [LICENSE](LICENSE) file for details.

---

**Have questions or ideas?** Feel free to open an issue or start a discussion!
