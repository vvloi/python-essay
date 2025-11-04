# Backend 3-Layer Architecture
# Business Logic Layer - Shopping List Service
from sqlalchemy.orm import Session
from typing import List
from backend.data_layer.repositories import RecipeRepository, PantryRepository
from backend import schemas


class ShoppingListService:
    """Service for shopping list generation business logic"""
    
    @staticmethod
    def generate_shopping_list(db: Session, recipe_ids: List[int]) -> List[schemas.ShoppingItem]:
        """Generate shopping list from multiple recipes, subtract pantry items"""
        ingredient_map = {}
        
        # Aggregate ingredients from all recipes
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
        
        # Get pantry items
        pantry_items = PantryRepository.get_all(db)
        pantry_map = {f"{p.name}_{p.unit}": p.quantity for p in pantry_items}
        
        # Calculate shopping list (needed - available)
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
