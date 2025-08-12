# NGINX Role

Sets up NGINX reverse proxy with SSL termination.

## Variables

- `nginx_image`: NGINX image (default: nginx:latest)
- `nginx_network_mode`: Network mode (default: host)
- `nginx_vhosts`: Virtual host configurations
- `ssl_type`: SSL type (default: selfsigned)

## Usage

```bash
ansible-playbook -i inventories/hosts site.yaml --tags nginx
```
