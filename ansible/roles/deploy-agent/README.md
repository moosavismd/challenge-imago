# Deploy Agent Role

Deploys lightweight deployment agent for CI/CD.

## Files

All agent files are included in the role:
- `files/agent.py` - Python Flask application
- `files/requirements.txt` - Python dependencies
- `files/Dockerfile` - Container build instructions
- `files/docker-compose.yaml` - Service definition

## Variables

- `deploy_agent_dir`: Agent directory
- `deploy_agent_port`: Agent port (default: 8080)
- `deploy_agent_token`: Authentication token
- `build_deploy_agent_image`: Build Docker image on host

## Usage

```bash
ansible-playbook -i inventories/hosts site.yaml --tags deploy-agent
```

## Test Commands

```bash
# Deploy new image
curl -X POST "http://localhost:8080/deploy" \
  -H "Authorization: Bearer my-secret-token" \
  -H "Content-Type: application/json" \
  -d '{"image_tag": "abc123"}'

# Check status
curl -X GET "http://localhost:8080/status"
```
