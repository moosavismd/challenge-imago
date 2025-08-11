# Pre-install Role

System preparation role for package management and Docker installation.

## Requirements

- Ansible 2.9+
- Ubuntu/Debian targets
- Root/sudo privileges

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `docker_version` | `"latest"` | Docker version to install |
| `update_package_cache` | `true` | Update package cache |
| `upgrade_packages` | `false` | Upgrade existing packages |
| `configure_dns` | `false` | Configure DNS settings |

## Usage

```yaml
- hosts: servers
  roles:
    - pre-install
  vars:
    docker_version: "24.0.5"
    upgrade_packages: true
```

## Features

- **Package management** (apt cache, upgrades)
- **Docker installation** (CE version)
- **DNS configuration** (systemd-resolved)
- **System preparation** for other roles
