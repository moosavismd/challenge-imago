# NGINX Role

Ansible role for deploying NGINX as a reverse proxy with SSL termination.

## Requirements

- Ansible 2.9+
- Docker
- `community.docker`, `community.crypto` collections

## Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ssl_type` | `"selfsigned"` | SSL certificate type |
| `domain_name` | `"example.com"` | Default domain |
| `nginx_image` | `"nginx:latest"` | NGINX Docker image |
| `nginx_container_name` | `"nginx"` | Container name |
| `nginx_network_mode` | `"host"` | Network mode (host for localhost access) |

## Configuration

```yaml
nginx_vhosts:
  - server_name: "api.example.com"
    backend_url: "http://localhost:8000"
    ssl_type: "selfsigned"
```

## Features

- **SSL termination** with self-signed certificates
- **Reverse proxy** to backend APIs
- **Host networking** for localhost access
- **Security headers** and SSL hardening
- **Docker container** deployment

## Usage

```yaml
- hosts: web_servers
  roles:
    - nginx
  vars:
    nginx_vhosts:
      - server_name: "api.example.com"
        backend_url: "http://localhost:8000"
```
