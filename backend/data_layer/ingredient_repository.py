# Backend 3-Layer Architecture
# Data Access Layer - Ingredient Repository
from sqlalchemy.orm import Session
from typing import List
from backend.models import Ingredient


class IngredientRepository:
    """Repository for Ingredient database operations"""
    
    @staticmethod
    def get_by_recipe_id(db: Session, recipe_id: int) -> List[Ingredient]:
        """Get all ingredients for a recipe"""
        return db.query(Ingredient).filter(Ingredient.recipe_id == recipe_id).all()
    
    @staticmethod
    def delete_by_recipe_id(db: Session, recipe_id: int):
        """Delete all ingredients for a recipe"""
        db.query(Ingredient).filter(Ingredient.recipe_id == recipe_id).delete()
        db.commit()
    
    @staticmethod
    def create_batch(db: Session, ingredients: List[Ingredient]):
        """Create multiple ingredients"""
        db.add_all(ingredients)
        db.commit()
