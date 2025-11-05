# Backend 3-Layer Architecture
# Data Access Layer - Pantry Repository
from sqlalchemy.orm import Session
from typing import List, Optional
from backend.models import Pantry


class PantryRepository:
    """Repository for Pantry database operations"""
    
    @staticmethod
    def get_all(db: Session) -> List[Pantry]:
        """Get all pantry items"""
        return db.query(Pantry).all()
    
    @staticmethod
    def get_by_id(db: Session, pantry_id: int) -> Optional[Pantry]:
        """Get pantry item by ID"""
        return db.query(Pantry).filter(Pantry.id == pantry_id).first()
    
    @staticmethod
    def get_by_name(db: Session, name: str) -> Optional[Pantry]:
        """Get pantry item by name"""
        return db.query(Pantry).filter(Pantry.name == name).first()
    
    @staticmethod
    def create(db: Session, pantry: Pantry) -> Pantry:
        """Create new pantry item"""
        db.add(pantry)
        db.commit()
        db.refresh(pantry)
        return pantry
    
    @staticmethod
    def update(db: Session, pantry: Pantry) -> Pantry:
        """Update existing pantry item"""
        db.commit()
        db.refresh(pantry)
        return pantry
    
    @staticmethod
    def delete(db: Session, pantry_id: int) -> bool:
        """Delete pantry item"""
        pantry = PantryRepository.get_by_id(db, pantry_id)
        if pantry:
            db.delete(pantry)
            db.commit()
            return True
        return False
