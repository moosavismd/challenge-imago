#!/usr/bin/env python3
"""
Simple test suite for Media Service API
"""

import requests

class TestAPI:
    """Simple API tests"""
    
    def test_home_endpoint(self):
        """Test home endpoint"""
        response = requests.get('http://localhost:8000/')
        assert response.status_code == 200
        data = response.json()
        assert data['message'] == 'Media Service API'
    
    def test_health_endpoint(self):
        """Test health endpoint"""
        response = requests.get('http://localhost:8000/health')
        assert response.status_code == 200
        assert response.json()['status'] == 'healthy'
    
    def test_random_endpoint(self):
        """Test random endpoint"""
        response = requests.get('http://localhost:8000/random')
        assert response.status_code == 200
        data = response.json()
        assert 1 <= data['number'] <= 1000
    
    def test_constant_endpoint(self):
        """Test constant endpoint"""
        response = requests.get('http://localhost:8000/cons')
        assert response.status_code == 200
        assert response.json()['number'] == 17

if __name__ == '__main__':
    import pytest
    pytest.main([__file__]) 