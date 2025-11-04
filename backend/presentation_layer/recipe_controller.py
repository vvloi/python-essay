# Backend 3-Layer Architecture
# Presentation Layer - Recipe Controller
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend import schemas
from backend.business_layer import RecipeService

router = APIRouter(prefix="/recipes", tags=["recipes"])


@router.get("", response_model=List[schemas.Recipe])
def get_recipes(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """Get all recipes with pagination"""
    return RecipeService.get_all_recipes(db, skip, limit)


@router.get("/search", response_model=List[schemas.Recipe])
def search_recipes(
    q: str = Query(..., min_length=1), 
    db: Session = Depends(get_db)
):
    """Search recipes by name"""
    return RecipeService.search_recipes(db, q)


@router.get("/{recipe_id}", response_model=schemas.Recipe)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """Get recipe by ID"""
    recipe = RecipeService.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.post("", response_model=schemas.Recipe, status_code=201)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    """Create new recipe"""
    return RecipeService.create_recipe(db, recipe)


@router.put("/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(
    recipe_id: int, 
    recipe: schemas.RecipeUpdate, 
    db: Session = Depends(get_db)
):
    """Update existing recipe"""
    updated_recipe = RecipeService.update_recipe(db, recipe_id, recipe)
    if not updated_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return updated_recipe


@router.delete("/{recipe_id}", status_code=204)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    """Delete recipe"""
    success = RecipeService.delete_recipe(db, recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recipe not found")


@router.get("/{recipe_id}/scale")
def scale_recipe(
    recipe_id: int, 
    factor: float = Query(..., gt=0), 
    db: Session = Depends(get_db)
):
    """Scale recipe ingredients by factor"""
    scaled = RecipeService.scale_recipe(db, recipe_id, factor)
    if not scaled:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return scaled
