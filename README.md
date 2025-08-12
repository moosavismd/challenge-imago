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

## CI/CD Support

This project supports both **GitLab CI** and **GitHub Actions** with identical functionality.

### GitLab CI Variables Required
Set these in GitLab CI/CD → Variables:
- `DEPLOY_TOKEN`: Your deployment token

### GitHub Actions Secrets Required  
Set these in GitHub → Settings → Secrets and variables → Actions:
- `DEPLOY_TOKEN`: Your deployment token
