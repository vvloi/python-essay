# Backend 3-Layer Architecture
# Business Logic Layer - Services
from sqlalchemy.orm import Session
from typing import List, Optional, Dict
from backend.data_layer.repositories import (
    RecipeRepository,
    IngredientRepository,
    StepRepository,
    PantryRepository
)
from backend.models import Recipe, Ingredient, Step, Pantry
from backend import schemas


class RecipeService:
    @staticmethod
    def get_all_recipes(db: Session, skip: int = 0, limit: int = 100) -> List[Recipe]:
        return RecipeRepository.get_all(db, skip, limit)

    @staticmethod
    def get_recipe(db: Session, recipe_id: int) -> Optional[Recipe]:
        return RecipeRepository.get_by_id(db, recipe_id)

    @staticmethod
    def search_recipes(db: Session, query: str) -> List[Recipe]:
        return RecipeRepository.search_by_name(db, query)

    @staticmethod
    def create_recipe(db: Session, recipe_data: schemas.RecipeCreate) -> Recipe:
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
        return RecipeRepository.delete(db, recipe_id)

    @staticmethod
    def scale_recipe(db: Session, recipe_id: int, scale_factor: float) -> Optional[Dict]:
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


class PantryService:
    @staticmethod
    def get_all_pantry_items(db: Session) -> List[Pantry]:
        return PantryRepository.get_all(db)

    @staticmethod
    def get_pantry_item(db: Session, pantry_id: int) -> Optional[Pantry]:
        return PantryRepository.get_by_id(db, pantry_id)

    @staticmethod
    def create_pantry_item(db: Session, pantry_data: schemas.PantryCreate) -> Pantry:
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
        pantry = PantryRepository.get_by_id(db, pantry_id)
        if not pantry:
            return None

        update_fields = pantry_data.model_dump(exclude_unset=True)
        for field, value in update_fields.items():
            setattr(pantry, field, value)

        return PantryRepository.update(db, pantry)

    @staticmethod
    def delete_pantry_item(db: Session, pantry_id: int) -> bool:
        return PantryRepository.delete(db, pantry_id)


class ShoppingListService:
    @staticmethod
    def generate_shopping_list(db: Session, recipe_ids: List[int]) -> List[schemas.ShoppingItem]:
        ingredient_map = {}

        for recipe_id in recipe_ids:
            recipe = RecipeRepository.get_by_id(db, recipe_id)
            if not recipe:
                continue

            for ingredient in recipe.ingredients:
                key = f"{ingredient.name}_{ingredient.unit}"

                if key in ingredient_map:
                    ingredient_map[key]["quantity"] += ingredient.quantity
                else:
                    ingredient_map[key] = {
                        "name": ingredient.name,
                        "quantity": ingredient.quantity,
                        "unit": ingredient.unit
                    }

        pantry_items = PantryRepository.get_all(db)
        pantry_map = {f"{p.name}_{p.unit}": p.quantity for p in pantry_items}

        shopping_list = []
        for key, item in ingredient_map.items():
            needed_quantity = item["quantity"]
            available_quantity = pantry_map.get(key, 0)

            remaining_quantity = max(0, needed_quantity - available_quantity)

            if remaining_quantity > 0:
                shopping_list.append(schemas.ShoppingItem(
                    name=item["name"],
                    quantity=remaining_quantity,
                    unit=item["unit"]
                ))

        return shopping_list
