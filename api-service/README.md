# API Service

Flask API server with Docker and GitLab CI/CD.

## API Endpoints

- `GET /` - Home with available routes
- `GET /health` - Health check
- `GET /random` - Random number (1-1000)
- `GET /cons` - Constant number (17)

## Quick Start

```bash
# Run directly
python api-server.py

# Run with Docker
docker-compose up -d
```

## Files

- `api-server.py` - Flask application
- `Dockerfile` - Container build
- `docker-compose.yml` - Local deployment
- `.gitlab-ci.yml` - CI/CD pipeline
- `requirements.txt` - Python dependencies
