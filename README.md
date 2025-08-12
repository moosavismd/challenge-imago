# Media Service Project

Infrastructure and API for media search and download service.

## Components

- **API Service** - Flask application and CI/CD (`api-service/`)
- **Deploy Agent** - Lightweight deployment service  
- **Infrastructure** - Ansible automation (`ansible/`)

## Quick Start

```bash
# Run API locally
cd api-service
python api-server.py

# Deploy complete infrastructure
cd ansible
ansible-playbook -i inventories/hosts site.yaml

# Deploy specific components
ansible-playbook -i inventories/hosts site.yaml --tags pre-install
ansible-playbook -i inventories/hosts site.yaml --tags nginx
ansible-playbook -i inventories/hosts site.yaml --tags deploy-agent
```

## Structure

- `api-service/` - API server, Docker, and CI/CD
- `deploy-agent/` - Deployment service
- `ansible/` - Infrastructure automation

## GitLab CI Variables Required

Set these in GitLab CI/CD → Variables:
- `DEPLOY_TOKEN`: Your deployment token
- `SERVER_A_IP`: Override if different from default
- `SERVER_B_IP`: Override if different from default
