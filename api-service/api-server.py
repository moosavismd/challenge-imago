#!/usr/bin/env python3
"""
Media Service API
- Simple Flask API for media search and download
- Endpoints: /random, /cons, /health
"""

from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/random')
def random_number():
    """Return a random number between 1 and 1000"""
    return jsonify({
        'number': random.randint(1, 1000),
        'endpoint': '/random'
    })

@app.route('/cons')
def constant_number():
    """Return the constant number 17"""
    return jsonify({
        'number': 18,
        'endpoint': '/cons'
    })

@app.route('/')
def home():
    """Home endpoint with available routes"""
    return jsonify({
        'message': 'Media Service API',
        'endpoints': {
            '/random': 'Returns a random number',
            '/cons': 'Returns the constant 17'
        }
    })

@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)
