# Pre-install Role

Prepares system with Docker and common packages.

## Variables

- `docker_version`: Docker version to install - multiple values: "latest" or specific version like "24.0.5" (default: "latest")
- `docker_install_method`: Docker installation method - single value: "docker-ce" (default: "docker-ce")
- `docker_repository_url`: Docker repository URL - single value (default: "https://download.docker.com/linux/ubuntu")
- `docker_gpg_key_url`: Docker GPG key URL - single value (default: "https://download.docker.com/linux/ubuntu/gpg")
- `install_docker_compose`: Install Docker Compose plugin - boolean: true/false (default: true)
- `update_package_cache`: Update package cache - boolean: true/false (default: true)
- `apt_cache_valid_time`: APT cache validity in seconds - numeric value (default: 3600)
- `upgrade_packages`: Upgrade OS packages - boolean: true/false (default: false)
- `common_packages`: List of packages to install - multiple values: list of package names (default: apt-transport-https, ca-certificates, curl, gnupg, lsb-release, software-properties-common)
- `configure_dns`: Configure DNS settings - boolean: true/false (default: false)
- `dns_nameservers`: DNS nameservers list - multiple values: list of IP addresses (default: ["178.22.122.100"])
- `reboot_after_upgrade`: Reboot after package upgrades - boolean: true/false (default: false)

## Tags

- `dns`: DNS configuration tasks
- `dns-setter`: DNS setting tasks

## Task Files

- `main.yaml`: Main pre-installation tasks
- `dns-setter.yaml`: DNS configuration tasks
- `docker.yaml`: Docker installation tasks

## Usage

```bash
# Deploy complete infrastructure
ansible-playbook -i inventories/hosts site.yaml --tags pre-install

# Deploy specific components
ansible-playbook -i inventories/hosts site.yaml --tags dns
```
