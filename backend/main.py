from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from backend.database import engine, Base
from backend.presentation_layer.routes import router

# Create database tables
Base.metadata.create_all(bind=engine)

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

# API routes
app.include_router(router, prefix="/api", tags=["recipes"])

# Serve frontend static files
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")


@app.get("/api/health")
def health_check():
    return {"status": "healthy", "architecture": "3-layer"}
