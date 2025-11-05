# Backend 3-Layer Architecture
# Data Access Layer - Recipe Repository
from sqlalchemy.orm import Session
from typing import List, Optional
from backend.models import Recipe


class RecipeRepository:
    """Repository for Recipe database operations"""
    
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Recipe]:
        """Get all recipes with pagination"""
        return db.query(Recipe).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_id(db: Session, recipe_id: int) -> Optional[Recipe]:
        """Get recipe by ID"""
        return db.query(Recipe).filter(Recipe.id == recipe_id).first()
    
    @staticmethod
    def search_by_name(db: Session, name: str) -> List[Recipe]:
        """Search recipes by name"""
        return db.query(Recipe).filter(Recipe.name.contains(name)).all()
    
    @staticmethod
    def create(db: Session, recipe: Recipe) -> Recipe:
        """Create new recipe"""
        db.add(recipe)
        db.commit()
        db.refresh(recipe)
        return recipe
    
    @staticmethod
    def update(db: Session, recipe: Recipe) -> Recipe:
        """Update existing recipe"""
        db.commit()
        db.refresh(recipe)
        return recipe
    
    @staticmethod
    def delete(db: Session, recipe_id: int) -> bool:
        """Delete recipe"""
        recipe = RecipeRepository.get_by_id(db, recipe_id)
        if recipe:
            db.delete(recipe)
            db.commit()
            return True
        return False
