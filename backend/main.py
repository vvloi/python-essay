from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.presentation_layer import recipe_controller, pantry_controller, shopping_list_controller
import os
from pathlib import Path

# NOTE: Database tables are managed by Alembic migrations.
# Automatic table creation has been removed to prevent inconsistencies and ensure proper migration tracking.
# Relying on migrations (similar to Liquibase changesets) allows for reliable schema management in production environments.
# To apply migrations, run: alembic upgrade head

app = FastAPI(
    title="Recipe Book API",
    description="3-Layer Architecture Recipe Management System",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API routes - separate controllers for better organization
app.include_router(recipe_controller.router, prefix="/api")
app.include_router(pantry_controller.router, prefix="/api")
app.include_router(shopping_list_controller.router, prefix="/api")

# Serve frontend static files. If a production build exists in frontend/dist use it,
# otherwise fall back to the development frontend folder so legacy files still work.
frontend_static = "frontend/dist" if Path("frontend/dist").exists() else "frontend"
app.mount("/", StaticFiles(directory=frontend_static, html=True), name="frontend")


@app.get("/api/health")
def health_check():
    return {"status": "healthy", "architecture": "3-layer"}
