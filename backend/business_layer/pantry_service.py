# Backend 3-Layer Architecture
# Business Logic Layer - Pantry Service
from sqlalchemy.orm import Session
from typing import List, Optional
from backend.data_layer.repositories import PantryRepository
from backend.models import Pantry
from backend import schemas


class PantryService:
    """Service for pantry inventory business logic"""
    
    @staticmethod
    def get_all_pantry_items(db: Session) -> List[Pantry]:
        """Get all pantry items"""
        return PantryRepository.get_all(db)
    
    @staticmethod
    def get_pantry_item(db: Session, pantry_id: int) -> Optional[Pantry]:
        """Get pantry item by ID"""
        return PantryRepository.get_by_id(db, pantry_id)
    
    @staticmethod
    def create_pantry_item(db: Session, pantry_data: schemas.PantryCreate) -> Pantry:
        """Create pantry item or update if exists"""
        existing = PantryRepository.get_by_name(db, pantry_data.name)
        if existing:
            existing.quantity += pantry_data.quantity
            existing.unit = pantry_data.unit
            return PantryRepository.update(db, existing)
        
        new_pantry = Pantry(
            name=pantry_data.name,
            quantity=pantry_data.quantity,
            unit=pantry_data.unit
        )
        return PantryRepository.create(db, new_pantry)
    
    @staticmethod
    def update_pantry_item(db: Session, pantry_id: int, pantry_data: schemas.PantryUpdate) -> Optional[Pantry]:
        """Update pantry item"""
        pantry = PantryRepository.get_by_id(db, pantry_id)
        if not pantry:
            return None
        
        update_fields = pantry_data.model_dump(exclude_unset=True)
        for field, value in update_fields.items():
            setattr(pantry, field, value)
        
        return PantryRepository.update(db, pantry)
    
    @staticmethod
    def delete_pantry_item(db: Session, pantry_id: int) -> bool:
        """Delete pantry item"""
        return PantryRepository.delete(db, pantry_id)
