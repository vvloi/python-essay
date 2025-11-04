# Backend 3-Layer Architecture
# Data Access Layer - Repository Pattern
from sqlalchemy.orm import Session
from typing import List, Optional
from backend.models import Recipe, Ingredient, Step, Pantry


class RecipeRepository:
    @staticmethod
    def get_all(db: Session, skip: int = 0, limit: int = 100) -> List[Recipe]:
        return db.query(Recipe).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_by_id(db: Session, recipe_id: int) -> Optional[Recipe]:
        return db.query(Recipe).filter(Recipe.id == recipe_id).first()
    
    @staticmethod
    def search_by_name(db: Session, name: str) -> List[Recipe]:
        return db.query(Recipe).filter(Recipe.name.contains(name)).all()
    
    @staticmethod
    def create(db: Session, recipe: Recipe) -> Recipe:
        db.add(recipe)
        db.commit()
        db.refresh(recipe)
        return recipe
    
    @staticmethod
    def update(db: Session, recipe: Recipe) -> Recipe:
        db.commit()
        db.refresh(recipe)
        return recipe
    
    @staticmethod
    def delete(db: Session, recipe_id: int) -> bool:
        recipe = RecipeRepository.get_by_id(db, recipe_id)
        if recipe:
            db.delete(recipe)
            db.commit()
            return True
        return False


class IngredientRepository:
    @staticmethod
    def get_by_recipe_id(db: Session, recipe_id: int) -> List[Ingredient]:
        return db.query(Ingredient).filter(Ingredient.recipe_id == recipe_id).all()
    
    @staticmethod
    def delete_by_recipe_id(db: Session, recipe_id: int):
        db.query(Ingredient).filter(Ingredient.recipe_id == recipe_id).delete()
        db.commit()
    
    @staticmethod
    def create_batch(db: Session, ingredients: List[Ingredient]):
        db.add_all(ingredients)
        db.commit()


class StepRepository:
    @staticmethod
    def get_by_recipe_id(db: Session, recipe_id: int) -> List[Step]:
        return db.query(Step).filter(Step.recipe_id == recipe_id).order_by(Step.step_number).all()
    
    @staticmethod
    def delete_by_recipe_id(db: Session, recipe_id: int):
        db.query(Step).filter(Step.recipe_id == recipe_id).delete()
        db.commit()
    
    @staticmethod
    def create_batch(db: Session, steps: List[Step]):
        db.add_all(steps)
        db.commit()


class PantryRepository:
    @staticmethod
    def get_all(db: Session) -> List[Pantry]:
        return db.query(Pantry).all()
    
    @staticmethod
    def get_by_id(db: Session, pantry_id: int) -> Optional[Pantry]:
        return db.query(Pantry).filter(Pantry.id == pantry_id).first()
    
    @staticmethod
    def get_by_name(db: Session, name: str) -> Optional[Pantry]:
        return db.query(Pantry).filter(Pantry.name == name).first()
    
    @staticmethod
    def create(db: Session, pantry: Pantry) -> Pantry:
        db.add(pantry)
        db.commit()
        db.refresh(pantry)
        return pantry
    
    @staticmethod
    def update(db: Session, pantry: Pantry) -> Pantry:
        db.commit()
        db.refresh(pantry)
        return pantry
    
    @staticmethod
    def delete(db: Session, pantry_id: int) -> bool:
        pantry = PantryRepository.get_by_id(db, pantry_id)
        if pantry:
            db.delete(pantry)
            db.commit()
            return True
        return False
