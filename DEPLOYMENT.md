# Deployment Guide

## Overview
This project uses a smart CI/CD pipeline that automatically detects changes and builds only the affected components.

## PostgreSQL Connection
- **Host**: `postgres.core-infra.svc.cluster.local:5432`
- **User**: `postgres`
- **Password**: `changeme`
- **Database**: `recipe_book`
- **Source**: Kubernetes namespace `core-infra`

## Automatic Database Setup
The backend uses Alembic to automatically create database tables on startup:
- When the container starts, it runs `alembic upgrade head`
- This creates all tables defined in `backend/models.py`
- No manual database initialization required

## Docker Images
Images are built and pushed to GitHub Container Registry:
- Backend: `ghcr.io/vvloi/python-essay/backend:latest`
- Frontend: `ghcr.io/vvloi/python-essay/frontend:latest`

## CI/CD Pipeline
The GitHub Actions workflow (`.github/workflows/ci.yml`) uses smart change detection:

### How it works:
1. **Change Detection**: Uses `dorny/paths-filter@v2` to detect which files changed
2. **Conditional Builds**:
   - If `backend/**` files changed → Build backend image
   - If `frontend/**` files changed → Build frontend image
   - If both changed → Build both images

### Triggers:
- Push to `main` branch
- Pull requests to `main` branch

### What happens on commit:
```
Commit in backend/ → Only backend image is built and pushed
Commit in frontend/ → Only frontend image is built and pushed
Commit in both → Both images are built and pushed
```

## Dockerfile Locations
- Backend: `backend/Dockerfile`
- Frontend: `frontend/Dockerfile`

Each Dockerfile is optimized for its respective service:
- **Backend**: Python 3.11, includes Alembic migrations, PostgreSQL client
- **Frontend**: Multi-stage build (Node.js builder + Nginx production)

## Deployment
Images are deployed using ArgoCD ApplicationSet (managed in separate repository).

## Testing Locally
To test the backend locally with PostgreSQL:
```powershell
# Set environment variable
$env:DATABASE_URL="postgresql://postgres:changeme@postgres.core-infra.svc.cluster.local:5432/recipe_book"

# Run migrations
alembic upgrade head

# Start backend
uvicorn backend.main:app --reload
```

To test the frontend locally:
```powershell
cd frontend
npm install
npm run dev
```

## Health Checks
- Backend health endpoint: `http://backend:8000/api/health`
- Configured in backend Dockerfile with 30s interval
