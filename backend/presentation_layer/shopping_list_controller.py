# Backend 3-Layer Architecture
# Presentation Layer - Shopping List Controller
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend import schemas
from backend.business_layer import ShoppingListService

router = APIRouter(prefix="/shopping-list", tags=["shopping-list"])


@router.post("", response_model=List[schemas.ShoppingItem])
def generate_shopping_list(
    recipe_ids: List[int], 
    db: Session = Depends(get_db)
):
    """Generate shopping list from selected recipes, subtract pantry items"""
    return ShoppingListService.generate_shopping_list(db, recipe_ids)
