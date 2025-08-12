# Deploy Agent Role

Deploys lightweight deployment agent for CI/CD.

## Variables

- `project_base_dir`: Base project directory (default: "/opt/media-service")
- `project_api_dir`: API directory path (default: "/opt/media-service/api")
- `project_deploy_agent_dir`: Deploy agent directory path (default: "/opt/media-service/deploy-agent")
- `project_nginx_dir`: NGINX directory path (default: "/opt/media-service/nginx")
- `deploy_agent_dir`: Deploy agent directory (default: "/opt/media-service/deploy-agent")
- `deploy_agent_port`: Agent port - numeric value (default: 8080)
- `deploy_agent_token`: Authentication token - single value (default: "{{ vault_deploy_token }}")
- `compose_dir`: Docker compose directory (default: "/opt/media-service/api")
- `deploy_agent_image_name`: Docker image name - single value (default: "deploy-agent")
- `deploy_agent_image_tag`: Docker image tag - single value (default: "latest")
- `build_deploy_agent_image`: Build Docker image on host - boolean: true/false (default: false)
- `registry_image`: Container registry image - single value (default: "ghcr.io/moosavismd/challenge-imago")
- `registry_username`: Registry username - single value (default: "{{ vault_registry_username }}")
- `registry_password`: Registry password - single value (default: "{{ vault_registry_password }}")

## Task Files

- `main.yaml`: Main deploy agent setup tasks

## Usage

```bash
# Deploy complete infrastructure
ansible-playbook -i inventories/hosts site.yaml --ask-vault-password
```
