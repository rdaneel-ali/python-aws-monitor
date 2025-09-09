"""Unit tests for the monitor module in python_health_monitor package."""
import pytest
from python_health_monitor import monitor

def test_check_url_success():
    """Test successful URL check."""
    ok, status = monitor.check_url("https://httpbin.org/status/200", "Test Success", timeout=10, retries=1)
    assert ok is True
    assert "Success: 200" in status

def test_check_url_failure():
    """Test failed URL check.""" 
    ok, status = monitor.check_url("https://httpbin.org/status/404", "Test Failure", timeout=10, retries=1)
    assert ok is False
    assert "Failed after" in status

def test_check_url_timeout():
    """Test timeout handling."""
    ok, status = monitor.check_url("https://httpbin.org/delay/10", "Test Timeout", timeout=2, retries=1)
    assert ok is False
    assert "Failed after" in status

if __name__ == "__main__":
    # Simple test runner
    print("Running tests...")
    
    try:
        test_check_url_success()
        print("✅ test_check_url_success passed")
    except Exception as e:
        print(f"❌ test_check_url_success failed: {e}")
    
    try:
        test_check_url_failure()
        print("✅ test_check_url_failure passed")
    except Exception as e:
        print(f"❌ test_check_url_failure failed: {e}")
        
    try:
        test_check_url_timeout()
        print("✅ test_check_url_timeout passed")
    except Exception as e:
        print(f"❌ test_check_url_timeout failed: {e}")
    
    print("Tests completed!")