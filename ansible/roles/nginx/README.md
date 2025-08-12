# NGINX Role

Sets up NGINX reverse proxy with SSL termination.

## Variables

- `project_base_dir`: Base project directory (default: "/opt/media-service")
- `project_nginx_dir`: NGINX directory path (default: "/opt/media-service/nginx")
- `ssl_type`: SSL type - single value: "selfsigned" (default: "selfsigned")
- `nginx_image`: NGINX image - single value (default: "nginx:latest")
- `nginx_container_name`: NGINX container name - single value (default: "nginx")
- `nginx_network_mode`: Network mode - single value: "host" (default: "host")
- `base_ssl_dir`: SSL directory path (default: "/opt/media-service/nginx/ssl")
- `base_nginx_conf_dir`: NGINX config directory path (default: "/opt/media-service/nginx/conf.d")
- `nginx_vhosts`: Virtual host configurations - multiple values: list of vhost objects (default: api.media-service.local, media.media-service.local)

## Task Files

- `main.yaml`: Main NGINX setup tasks
- `add-config.yaml`: Virtual host configuration deployment
- `ssl_selfsigned.yaml`: Self-signed SSL certificate generation
- `ssl_hardening.yaml`: SSL security hardening configuration

## Usage

```bash
# Deploy complete infrastructure
ansible-playbook -i inventories/hosts site.yaml --ask-vault-password
```
