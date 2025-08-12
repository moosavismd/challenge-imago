# Ansible Infrastructure

Media service infrastructure automation.

## Quick Start

```bash
ansible-playbook -i inventories/hosts site.yaml
```

## Tags

- `pre-install` - System preparation
- `nginx` - NGINX reverse proxy
- `deploy-agent` - Deployment service
- `always` - Always run (pre-install, zabbix)

## Structure

- `roles/` - Ansible roles
- `inventories/` - Server definitions
- `site.yaml` - Main playbook
