#!/usr/bin/env python3
"""
Lightweight Deploy Agent
- Listens on port 8080
- Basic authentication
- Updates docker-compose.yml with new image tag
- Runs docker-compose up -d
"""

import os
import json
import subprocess
import yaml
import logging
from flask import Flask, request, jsonify
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('/var/log/deploy-agent.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Configuration
DEPLOY_TOKEN = os.environ.get('DEPLOY_TOKEN', 'my-secret-token')
COMPOSE_FILE = os.environ.get('COMPOSE_FILE', 'docker-compose.yml')
COMPOSE_DIR = os.environ.get('COMPOSE_DIR', '/opt/media-service/api')
PORT = int(os.environ.get('PORT', 8080))

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'service': 'deploy-agent'
    })

@app.route('/status', methods=['GET'])
def status():
    """Get current deployment status"""
    try:
        # Check if docker-compose is running
        result = subprocess.run(
            ['docker-compose', '-f', COMPOSE_FILE, 'ps', '--format', 'json'],
            cwd=COMPOSE_DIR,
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            return jsonify({
                'status': 'running',
                'compose_file': COMPOSE_FILE,
                'working_dir': COMPOSE_DIR,
                'docker_status': result.stdout
            })
        else:
            return jsonify({
                'status': 'stopped',
                'error': result.stderr
            })
    except Exception as e:
        logger.error(f"Error checking status: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/deploy', methods=['POST'])
def deploy():
    """Deploy new image version"""
    # Check authentication
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != f'Bearer {DEPLOY_TOKEN}':
        logger.warning("Unauthorized deployment attempt")
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Get image tag from request
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        image_tag = data.get('image_tag')
        if not image_tag:
            return jsonify({'error': 'image_tag required'}), 400
        
        logger.info(f"Starting deployment with image tag: {image_tag}")
        
        # Update docker-compose.yml
        if not update_docker_compose(image_tag):
            return jsonify({'error': 'Failed to update docker-compose.yml'}), 500
        
        # Deploy with docker-compose
        deploy_result = deploy_with_compose()
        if not deploy_result:
            return jsonify({'error': 'Deployment failed'}), 500
        
        logger.info(f"Deployment completed successfully with tag: {image_tag}")
        return jsonify({
            'status': 'success',
            'message': f'Deployed image tag: {image_tag}',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Deployment error: {e}")
        return jsonify({'error': str(e)}), 500

def update_docker_compose(image_tag):
    """Update docker-compose.yml with new image tag"""
    try:
        compose_path = os.path.join(COMPOSE_DIR, COMPOSE_FILE)
        
        if not os.path.exists(compose_path):
            logger.error(f"Docker compose file not found: {compose_path}")
            return False
        
        # Read current docker-compose.yml
        with open(compose_path, 'r') as f:
            compose_data = yaml.safe_load(f)
        
        # Update image tag for the main service
        if 'services' in compose_data:
            for service_name, service_config in compose_data['services'].items():
                if 'image' in service_config:
                    # Handle both tagged and untagged images
                    if ':' in service_config['image']:
                        # Image already has a tag, extract base name
                        base_image = service_config['image'].split(':')[0]
                    else:
                        # Image has no tag, use as is
                        base_image = service_config['image']
                    
                    service_config['image'] = f"{base_image}:{image_tag}"
                    logger.info(f"Updated {service_name} image to: {service_config['image']}")
        
        # Write updated docker-compose.yml
        with open(compose_path, 'w') as f:
            yaml.dump(compose_data, f, default_flow_style=False)
        
        logger.info(f"Updated {compose_path} with image tag: {image_tag}")
        return True
        
    except Exception as e:
        logger.error(f"Error updating docker-compose.yml: {e}")
        return False

def deploy_with_compose():
    """Run docker-compose up -d"""
    try:
        logger.info(f"Running docker-compose up -d in {COMPOSE_DIR}")
        
        # Pull latest images
        pull_result = subprocess.run(
            ['docker-compose', '-f', COMPOSE_FILE, 'pull'],
            cwd=COMPOSE_DIR,
            capture_output=True,
            text=True
        )
        
        if pull_result.returncode != 0:
            logger.warning(f"Image pull warning: {pull_result.stderr}")
        
        # Start services
        up_result = subprocess.run(
            ['docker-compose', '-f', COMPOSE_FILE, 'up', '-d'],
            cwd=COMPOSE_DIR,
            capture_output=True,
            text=True
        )
        
        if up_result.returncode == 0:
            logger.info("Docker-compose up -d completed successfully")
            return True
        else:
            logger.error(f"Docker-compose up -d failed: {up_result.stderr}")
            return False
            
    except Exception as e:
        logger.error(f"Error running docker-compose: {e}")
        return False

@app.route('/rollback', methods=['POST'])
def rollback():
    """Rollback to previous image version"""
    # Check authentication
    auth_header = request.headers.get('Authorization')
    if not auth_header or auth_header != f'Bearer {DEPLOY_TOKEN}':
        logger.warning("Unauthorized rollback attempt")
        return jsonify({'error': 'Unauthorized'}), 401
    
    # Get previous tag from request
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        previous_tag = data.get('previous_tag')
        if not previous_tag:
            return jsonify({'error': 'previous_tag required'}), 400
        
        logger.info(f"Starting rollback to image tag: {previous_tag}")
        
        # Update docker-compose.yml
        if not update_docker_compose(previous_tag):
            return jsonify({'error': 'Failed to update docker-compose.yml'}), 500
        
        # Deploy with docker-compose
        deploy_result = deploy_with_compose()
        if not deploy_result:
            return jsonify({'error': 'Rollback failed'}), 500
        
        logger.info(f"Rollback completed successfully to tag: {previous_tag}")
        return jsonify({
            'status': 'success',
            'message': f'Rolled back to image tag: {previous_tag}',
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        logger.error(f"Rollback error: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT, debug=False)
