#!/usr/bin/env python3
"""
Test suite for Media Service API
"""

import pytest
import json
import subprocess
import time
import requests
import signal
import os

class TestAPIEndpoints:
    """Test all API endpoints using HTTP requests"""
    
    @pytest.fixture(scope="class")
    def api_server(self):
        """Start the API server for testing"""
        # Start the server in background
        process = subprocess.Popen(
            ['python', 'api-server.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        # Wait for server to start
        time.sleep(5)
        
        yield process
        
        # Cleanup: stop the server
        process.terminate()
        process.wait()
    
    def test_home_endpoint(self, api_server):
        """Test the home endpoint returns correct structure"""
        response = requests.get('http://localhost:8000/')
        assert response.status_code == 200
        
        data = response.json()
        assert 'message' in data
        assert 'endpoints' in data
        assert data['message'] == 'Media Service API'
        assert '/random' in data['endpoints']
        assert '/cons' in data['endpoints']
    
    def test_health_endpoint(self, api_server):
        """Test the health endpoint returns healthy status"""
        response = requests.get('http://localhost:8000/health')
        assert response.status_code == 200
        
        data = response.json()
        assert 'status' in data
        assert data['status'] == 'healthy'
    
    def test_random_endpoint(self, api_server):
        """Test the random endpoint returns valid random number"""
        response = requests.get('http://localhost:8000/random')
        assert response.status_code == 200
        
        data = response.json()
        assert 'number' in data
        assert 'endpoint' in data
        assert data['endpoint'] == '/random'
        assert isinstance(data['number'], int)
        assert 1 <= data['number'] <= 1000
    
    def test_constant_endpoint(self, api_server):
        """Test the constant endpoint returns 17"""
        response = requests.get('http://localhost:8000/cons')
        assert response.status_code == 200
        
        data = response.json()
        assert 'number' in data
        assert 'endpoint' in data
        assert data['endpoint'] == '/cons'
        assert data['number'] == 17
    
    def test_nonexistent_endpoint(self, api_server):
        """Test that nonexistent endpoints return 404"""
        response = requests.get('http://localhost:8000/nonexistent')
        assert response.status_code == 404

class TestAPIResponseFormat:
    """Test API response format consistency"""
    
    @pytest.fixture(scope="class")
    def api_server(self):
        """Start the API server for testing"""
        process = subprocess.Popen(
            ['python', 'api-server.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        time.sleep(5)
        yield process
        process.terminate()
        process.wait()
    
    def test_all_endpoints_return_json(self, api_server):
        """Test that all endpoints return valid JSON"""
        endpoints = ['/', '/health', '/random', '/cons']
        
        for endpoint in endpoints:
            response = requests.get(f'http://localhost:8000{endpoint}')
            assert response.status_code == 200
            assert response.headers['content-type'] == 'application/json'
            
            # Verify JSON is valid
            try:
                response.json()
            except json.JSONDecodeError:
                pytest.fail(f"Endpoint {endpoint} returned invalid JSON")

class TestAPIFunctionality:
    """Test API functionality and edge cases"""
    
    @pytest.fixture(scope="class")
    def api_server(self):
        """Start the API server for testing"""
        process = subprocess.Popen(
            ['python', 'api-server.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        time.sleep(5)
        yield process
        process.terminate()
        process.wait()
    
    def test_random_numbers_are_different(self, api_server):
        """Test that random endpoint returns different numbers"""
        responses = []
        for _ in range(5):
            response = requests.get('http://localhost:8000/random')
            data = response.json()
            responses.append(data['number'])
        
        # Check that we get at least some different numbers
        unique_numbers = set(responses)
        assert len(unique_numbers) >= 2, "Random endpoint should return different numbers"
    
    def test_constant_always_same(self, api_server):
        """Test that constant endpoint always returns 17"""
        for _ in range(3):
            response = requests.get('http://localhost:8000/cons')
            data = response.json()
            assert data['number'] == 17

if __name__ == '__main__':
    pytest.main([__file__]) 