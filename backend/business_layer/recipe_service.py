# Backend 3-Layer Architecture
# Business Logic Layer - Recipe Service
from sqlalchemy.orm import Session
from typing import List, Optional, Dict
from backend.data_layer.repositories import (
    RecipeRepository, 
    IngredientRepository, 
    StepRepository
)
from backend.models import Recipe, Ingredient, Step
from backend import schemas


class RecipeService:
    """Service for recipe business logic"""
    
    @staticmethod
    def get_all_recipes(db: Session, skip: int = 0, limit: int = 100) -> List[Recipe]:
        """Get all recipes with pagination"""
        return RecipeRepository.get_all(db, skip, limit)

    @staticmethod
    def get_recipe(db: Session, recipe_id: int) -> Optional[Recipe]:
        """Get recipe by ID"""
        return RecipeRepository.get_by_id(db, recipe_id)

    @staticmethod
    def search_recipes(db: Session, query: str) -> List[Recipe]:
        """Search recipes by name"""
        return RecipeRepository.search_by_name(db, query)

    @staticmethod
    def create_recipe(db: Session, recipe_data: schemas.RecipeCreate) -> Recipe:
        """Create new recipe with ingredients and steps"""
        new_recipe = Recipe(
            name=recipe_data.name,
            description=recipe_data.description,
            cuisine=recipe_data.cuisine,
            servings=recipe_data.servings,
            prep_time_minutes=recipe_data.prep_time_minutes,
            cook_time_minutes=recipe_data.cook_time_minutes
        )

        saved_recipe = RecipeRepository.create(db, new_recipe)

        if recipe_data.ingredients:
            ingredients = [
                Ingredient(
                    recipe_id=saved_recipe.id,
                    name=ing.name,
                    quantity=ing.quantity,
                    unit=ing.unit
                )
                for ing in recipe_data.ingredients
            ]
            IngredientRepository.create_batch(db, ingredients)

        if recipe_data.steps:
            steps = [
                Step(
                    recipe_id=saved_recipe.id,
                    step_number=step.step_number,
                    instruction=step.instruction
                )
                for step in recipe_data.steps
            ]
            StepRepository.create_batch(db, steps)

        return RecipeRepository.get_by_id(db, saved_recipe.id)

    @staticmethod
    def update_recipe(db: Session, recipe_id: int, recipe_data: schemas.RecipeUpdate) -> Optional[Recipe]:
        """Update existing recipe"""
        recipe = RecipeRepository.get_by_id(db, recipe_id)
        if not recipe:
            return None

        update_fields = recipe_data.model_dump(exclude_unset=True)

        for field, value in update_fields.items():
            if field == "ingredients":
                IngredientRepository.delete_by_recipe_id(db, recipe_id)
                if value:
                    ingredients = [
                        Ingredient(
                            recipe_id=recipe_id,
                            name=ing.name,
                            quantity=ing.quantity,
                            unit=ing.unit
                        )
                        for ing in value
                    ]
                    IngredientRepository.create_batch(db, ingredients)
            elif field == "steps":
                StepRepository.delete_by_recipe_id(db, recipe_id)
                if value:
                    steps = [
                        Step(
                            recipe_id=recipe_id,
                            step_number=step.step_number,
                            instruction=step.instruction
                        )
                        for step in value
                    ]
                    StepRepository.create_batch(db, steps)
            else:
                setattr(recipe, field, value)

        return RecipeRepository.update(db, recipe)

    @staticmethod
    def delete_recipe(db: Session, recipe_id: int) -> bool:
        """Delete recipe"""
        return RecipeRepository.delete(db, recipe_id)

    @staticmethod
    def scale_recipe(db: Session, recipe_id: int, scale_factor: float) -> Optional[Dict]:
        """Scale recipe ingredients by factor"""
        recipe = RecipeRepository.get_by_id(db, recipe_id)
        if not recipe:
            return None

        scaled_ingredients = [
            {
                "name": ing.name,
                "quantity": ing.quantity * scale_factor,
                "unit": ing.unit
            }
            for ing in recipe.ingredients
        ]

        return {
            "original_servings": recipe.servings,
            "scaled_servings": int(recipe.servings * scale_factor),
            "scale_factor": scale_factor,
            "ingredients": scaled_ingredients
        }