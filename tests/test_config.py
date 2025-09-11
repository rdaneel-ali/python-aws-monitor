from pathlib import Path
from unittest.mock import patch

import pytest

from python_health_monitor.monitor import load_config, load_yaml


# The 'fs' fixture is provided by pyfakefs
def test_load_yaml_success(fs):
    """Test successful loading of a valid YAML file."""
    # Create a fake config file in the in-memory file system
    config_data = """
    key1: value1
    key2:
      - item1
      - item2
    """
    fs.create_file("/fake_config.yaml", contents=config_data)

    # Call the function with the fake file path
    path = Path("/fake_config.yaml")
    config = load_yaml(path)

    # Assert that the function returned the correct dictionary
    assert config == {"key1": "value1", "key2": ["item1", "item2"]}


def test_load_yaml_file_not_found(fs):
    """Test behavior when the config file does not exist."""
    # The file is not created, so it shouldn't exist
    path = Path("/nonexistent_config.yaml")
    config = load_yaml(path)

    # Assert that an empty dictionary is returned
    assert config == {}


def test_load_yaml_invalid_yaml(fs):
    """Test behavior with malformed YAML content."""
    # Create a fake file with invalid YAML
    invalid_data = "key: [invalid"
    fs.create_file("/invalid_config.yaml", contents=invalid_data)

    path = Path("/invalid_config.yaml")
    config = load_yaml(path)

    # Assert that an empty dictionary is returned
    assert config == {}


# Fixture to mock the project root
@pytest.fixture
def mock_project_root(fs):
    """Fixture to mock the PROJECT_ROOT variable."""

    # Mock the project root to a known location in the fake FS
    fs.create_dir("/mock_project_root/config")
    fs.create_dir("/mock_project_root/logs")
    return Path("/mock_project_root")


def test_load_config_default_found(fs, mock_project_root):
    """Test loading the default config file successfully."""
    # Use a mock for PROJECT_ROOT to control the path
    with patch("python_health_monitor.monitor.PROJECT_ROOT", new=mock_project_root):
        with patch("python_health_monitor.monitor.load_yaml") as mock_load_yaml:
            mock_load_yaml.return_value = {"monitor": {"timeout": 10}}
            # Test with no explicit path, so it uses the default
            config = load_config(None)
            assert config["monitor"]["timeout"] == 10


def test_load_config_explicit_path_found(fs, mock_project_root):
    """Test loading an explicitly specified config file successfully."""
    with patch("python_health_monitor.monitor.PROJECT_ROOT", new=mock_project_root):
        config_data = """
            monitor:
            retries: 5
        """
        fs.create_file("/mock_project_root/my_custom_config.yaml", contents=config_data)

        # Test with an explicit path provided via CLI
        config = load_config("/mock_project_root/my_custom_config.yaml")
        assert config["monitor"]["retries"] == 5


def test_load_config_explicit_path_not_found(fs, mock_project_root, capsys):
    """Test behavior when an explicitly specified config file is not found."""
    with patch("python_health_monitor.monitor.PROJECT_ROOT", new=mock_project_root):
        config = load_config("/mock_project_root/nonexistent_config.yaml")

        assert config == {}
        # Check if the correct error message was printed
        captured = capsys.readouterr()
        assert "ERROR: Specified config file not found" in captured.out


def test_load_config_fallback(fs, mock_project_root):
    """Test fallback to default configuration when no file exists."""
    with patch("python_health_monitor.monitor.PROJECT_ROOT", new=mock_project_root):
        # No config file is created, so the function should fall back
        config = load_config(None)
        assert config["endpoints"] == []
        assert config["monitor"]["timeout"] == 5
