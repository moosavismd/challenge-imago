# Challenge Imago - Media Service Infrastructure

## 🎯 Overview

A complete CI/CD pipeline and infrastructure automation solution demonstrating **infrastructure as code**, **automated deployment**, and **CI/CD best practices**.

## 🏗️ Architecture

```
CI/CD Pipeline → Container Registry → Load Balancer → Servers A & B
```

## 🚀 Key Features

- **CI/CD Pipeline**: GitHub Actions / GitLab CI with rolling deployments
- **Infrastructure**: Ansible automation for server provisioning
- **Containerization**: Docker + Nginx reverse proxy
- **High Availability**: Multi-server deployment with load balancing
- **Security**: SSL termination and authentication

## 📁 Project Structure

```
├── .github/workflows/    # GitHub Actions CI/CD
├── api-service/          # Flask API + Docker + Tests
├── ansible/              # Infrastructure automation
└── haproxy.cfg           # Load balancer config
```

## 🔧 Components

### API Server
Simple Flask application with 4 endpoints: home (`/`), health check (`/health`), random number (`/random`), and constant value (`/cons`). Serves as a lightweight service to demonstrate the infrastructure and deployment pipeline.

### Deploy Agent
Python Flask service running on each server that handles deployment requests from CI/CD pipeline. Receives image tags, pulls Docker images, updates docker-compose files, and manages container lifecycle. Deployed via Ansible as a systemd service with Docker containerization.

## 🚀 Quick Start

### Prerequisites
- Python 3.8+, Docker, Ansible 2.12+

### Setup
```bash
# Clone and install dependencies
git clone <repo-url>
cd challenge-imago

# Install Ansible collections
ansible-galaxy collection install community.docker community.crypto

# Install Python packages
cd api-service && pip install -r requirements.txt
```

### Run Locally
```bash
cd api-service
python api-server.py
# API available at http://localhost:8000
```

### Deploy Infrastructure
```bash
cd ansible
ansible-playbook -i inventories/hosts site.yaml --skip-tags verify --ask-vault-password
```

## 🧪 Testing

```bash
cd api-service
python -m pytest test_api.py -v
```

## 🔧 Configuration

Update server IPs in:
- `.github/workflows/ci-cd.yaml`
- `ansible/inventories/hosts`
- `haproxy.cfg`

## 📝 What This Demonstrates

- **Infrastructure as Code** with Ansible roles
- **CI/CD pipeline** design and implementation  
- **Container orchestration** and management
- **Multi-server deployment** strategies
- **Production-ready patterns** and best practices

## ⚠️ Scope & Limitations

- **Included**: Complete CI/CD, infrastructure automation, multi-server deployment
- **Simplified**: Basic Flask API (4 endpoints), self-signed SSL, basic monitoring
- **Production**: Would add advanced monitoring, security, backup/recovery

## 🔄 Deployment Flow

1. Push code → Triggers CI/CD
2. Run tests → Unit + integration tests
3. Build image → Docker + push to registry
4. Deploy A → Update Server A, verify health
5. Deploy B → Update Server B, verify health
6. Complete → Both servers running new version

---

**Focus: Infrastructure automation and deployment pipeline, not complex API logic.**
