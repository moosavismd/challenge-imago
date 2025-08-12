# Pre-install Role

Prepares system with Docker and common packages.

## Variables

- `docker_install_method`: Docker installation method
- `upgrade_packages`: Upgrade OS packages
- `configure_dns`: Configure DNS settings
- `common_packages`: List of packages to install

## Usage

```bash
ansible-playbook -i inventories/hosts site.yaml --tags pre-install
```
