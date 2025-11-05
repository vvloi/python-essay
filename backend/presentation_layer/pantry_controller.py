# Backend 3-Layer Architecture
# Presentation Layer - Pantry Controller
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend import schemas
from backend.business_layer import PantryService

router = APIRouter(prefix="/pantry", tags=["pantry"])


@router.get("", response_model=List[schemas.Pantry])
def get_pantry_items(db: Session = Depends(get_db)):
    """Get all pantry items"""
    return PantryService.get_all_pantry_items(db)


@router.get("/{pantry_id}", response_model=schemas.Pantry)
def get_pantry_item(pantry_id: int, db: Session = Depends(get_db)):
    """Get pantry item by ID"""
    pantry = PantryService.get_pantry_item(db, pantry_id)
    if not pantry:
        raise HTTPException(status_code=404, detail="Pantry item not found")
    return pantry


@router.post("", response_model=schemas.Pantry, status_code=201)
def create_pantry_item(pantry: schemas.PantryCreate, db: Session = Depends(get_db)):
    """Create new pantry item or update if exists"""
    return PantryService.create_pantry_item(db, pantry)


@router.put("/{pantry_id}", response_model=schemas.Pantry)
def update_pantry_item(
    pantry_id: int, 
    pantry: schemas.PantryUpdate, 
    db: Session = Depends(get_db)
):
    """Update pantry item"""
    updated = PantryService.update_pantry_item(db, pantry_id, pantry)
    if not updated:
        raise HTTPException(status_code=404, detail="Pantry item not found")
    return updated


@router.delete("/{pantry_id}", status_code=204)
def delete_pantry_item(pantry_id: int, db: Session = Depends(get_db)):
    """Delete pantry item"""
    success = PantryService.delete_pantry_item(db, pantry_id)
    if not success:
        raise HTTPException(status_code=404, detail="Pantry item not found")
