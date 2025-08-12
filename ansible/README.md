# Ansible Infrastructure

Media service infrastructure automation.

## Package Installation

### Prerequisites
- Python 3.8+
- Ansible 2.12+

### Install Required Collections
```bash
# Install community.docker and community.crypto collections
ansible-galaxy collection install community.docker
ansible-galaxy collection install community.crypto

# Or install from requirements file
ansible-galaxy collection install -r collections/requirements.yaml
```

### Install Dependencies
```bash
# Install required Python packages
pip install -r requirements.txt

# Or install manually
pip install docker pyyaml cryptography
```

## Variables

- `install_pre_install`: Install pre-installation packages - boolean: true/false (default: true)
- `install_zabbix`: Install Zabbix monitoring agent - boolean: true/false (default: true)

## Playbooks

- `site.yaml`: Main playbook for complete infrastructure setup

## Task Files

- `site.yaml`: Main playbook with role execution logic

## Usage

```bash
# Deploy complete infrastructure
ansible-playbook -i inventories/hosts site.yaml --skip-tags verify

# Deploy and configure Nginx
ansible-playbook -i inventories/hosts site.yaml -t nginx


# Deploy Deployer agent
ansible-playbook -i inventories/hosts site.yaml --skip-tags verify -t deploy-agent
```
