# Media Service API

Simple Flask API for media search and download service.

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python api-server.py

# Or with Docker
docker build -t media-service .
docker run -p 8000:8000 media-service

# Or with Docker Compose
docker-compose up -d
```

## Endpoints

- `/` - Home with available routes
- `/random` - Returns random number 1-1000
- `/cons` - Returns constant 17
- `/health` - Health check endpoint

## Files

- `api-server.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `Dockerfile` - Container build instructions
- `docker-compose.yaml` - Local deployment
