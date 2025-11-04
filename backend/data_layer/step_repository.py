# Backend 3-Layer Architecture
# Data Access Layer - Step Repository
from sqlalchemy.orm import Session
from typing import List
from backend.models import Step


class StepRepository:
    """Repository for Step database operations"""
    
    @staticmethod
    def get_by_recipe_id(db: Session, recipe_id: int) -> List[Step]:
        """Get all steps for a recipe, ordered by step_number"""
        return db.query(Step).filter(Step.recipe_id == recipe_id).order_by(Step.step_number).all()
    
    @staticmethod
    def delete_by_recipe_id(db: Session, recipe_id: int):
        """Delete all steps for a recipe"""
        db.query(Step).filter(Step.recipe_id == recipe_id).delete()
        db.commit()
    
    @staticmethod
    def create_batch(db: Session, steps: List[Step]):
        """Create multiple steps"""
        db.add_all(steps)
        db.commit()
