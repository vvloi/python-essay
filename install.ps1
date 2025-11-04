# Installation Script for Recipe Book
# Run this if requirements.txt fails

Write-Host "Installing Recipe Book dependencies..." -ForegroundColor Green

# Upgrade pip first
Write-Host "`nUpgrading pip..." -ForegroundColor Yellow
python -m pip install --upgrade pip

# Install core dependencies
Write-Host "`nInstalling FastAPI..." -ForegroundColor Yellow
pip install fastapi

Write-Host "`nInstalling Uvicorn..." -ForegroundColor Yellow
pip install "uvicorn[standard]"

Write-Host "`nInstalling SQLAlchemy..." -ForegroundColor Yellow
pip install sqlalchemy

Write-Host "`nInstalling Alembic..." -ForegroundColor Yellow
pip install alembic

Write-Host "`nInstalling Python-dotenv..." -ForegroundColor Yellow
pip install python-dotenv

Write-Host "`nInstalling Pydantic..." -ForegroundColor Yellow
pip install pydantic

Write-Host "`nInstalling Pydantic-settings..." -ForegroundColor Yellow
pip install pydantic-settings

Write-Host "`nInstalling Requests..." -ForegroundColor Yellow
pip install requests

Write-Host "`n✓ All dependencies installed successfully!" -ForegroundColor Green
Write-Host "`nYou can now run:" -ForegroundColor Cyan
Write-Host "  alembic upgrade head" -ForegroundColor White
Write-Host "  uvicorn backend.main:app --reload" -ForegroundColor White
