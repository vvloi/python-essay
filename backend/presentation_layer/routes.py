# Backend 3-Layer Architecture
# Presentation Layer - API Controllers/Routes
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from backend.database import get_db
from backend import schemas
from backend.business_layer.services import RecipeService, PantryService, ShoppingListService

router = APIRouter()


# Recipe Endpoints
@router.get("/recipes", response_model=List[schemas.Recipe])
def get_recipes(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    return RecipeService.get_all_recipes(db, skip, limit)


@router.get("/recipes/search", response_model=List[schemas.Recipe])
def search_recipes(
    q: str = Query(..., min_length=1),
    db: Session = Depends(get_db)
):
    return RecipeService.search_recipes(db, q)


@router.get("/recipes/{recipe_id}", response_model=schemas.Recipe)
def get_recipe(recipe_id: int, db: Session = Depends(get_db)):
    recipe = RecipeService.get_recipe(db, recipe_id)
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.post("/recipes", response_model=schemas.Recipe, status_code=201)
def create_recipe(recipe: schemas.RecipeCreate, db: Session = Depends(get_db)):
    return RecipeService.create_recipe(db, recipe)


@router.put("/recipes/{recipe_id}", response_model=schemas.Recipe)
def update_recipe(
    recipe_id: int,
    recipe: schemas.RecipeUpdate,
    db: Session = Depends(get_db)
):
    updated_recipe = RecipeService.update_recipe(db, recipe_id, recipe)
    if not updated_recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return updated_recipe


@router.delete("/recipes/{recipe_id}", status_code=204)
def delete_recipe(recipe_id: int, db: Session = Depends(get_db)):
    success = RecipeService.delete_recipe(db, recipe_id)
    if not success:
        raise HTTPException(status_code=404, detail="Recipe not found")


@router.get("/recipes/{recipe_id}/scale")
def scale_recipe(
    recipe_id: int,
    factor: float = Query(..., gt=0),
    db: Session = Depends(get_db)
):
    scaled = RecipeService.scale_recipe(db, recipe_id, factor)
    if not scaled:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return scaled


# Pantry Endpoints
@router.get("/pantry", response_model=List[schemas.Pantry])
def get_pantry_items(db: Session = Depends(get_db)):
    return PantryService.get_all_pantry_items(db)


@router.get("/pantry/{pantry_id}", response_model=schemas.Pantry)
def get_pantry_item(pantry_id: int, db: Session = Depends(get_db)):
    pantry = PantryService.get_pantry_item(db, pantry_id)
    if not pantry:
        raise HTTPException(status_code=404, detail="Pantry item not found")
    return pantry


@router.post("/pantry", response_model=schemas.Pantry, status_code=201)
def create_pantry_item(pantry: schemas.PantryCreate, db: Session = Depends(get_db)):
    return PantryService.create_pantry_item(db, pantry)


@router.put("/pantry/{pantry_id}", response_model=schemas.Pantry)
def update_pantry_item(
    pantry_id: int,
    pantry: schemas.PantryUpdate,
    db: Session = Depends(get_db)
):
    updated = PantryService.update_pantry_item(db, pantry_id, pantry)
    if not updated:
        raise HTTPException(status_code=404, detail="Pantry item not found")
    return updated


@router.delete("/pantry/{pantry_id}", status_code=204)
def delete_pantry_item(pantry_id: int, db: Session = Depends(get_db)):
    success = PantryService.delete_pantry_item(db, pantry_id)
    if not success:
        raise HTTPException(status_code=404, detail="Pantry item not found")


# Shopping List Endpoint
@router.post("/shopping-list", response_model=List[schemas.ShoppingItem])
def generate_shopping_list(
    recipe_ids: List[int],
    db: Session = Depends(get_db)
):
    return ShoppingListService.generate_shopping_list(db, recipe_ids)
