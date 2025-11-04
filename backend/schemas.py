from pydantic import BaseModel, Field
from typing import List, Optional


class IngredientBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    quantity: float = Field(..., gt=0)
    unit: str = Field(..., min_length=1, max_length=50)


class IngredientCreate(IngredientBase):
    pass


class Ingredient(IngredientBase):
    id: int
    recipe_id: int
    
    class Config:
        from_attributes = True


class StepBase(BaseModel):
    step_number: int = Field(..., gt=0)
    instruction: str = Field(..., min_length=1)


class StepCreate(StepBase):
    pass


class Step(StepBase):
    id: int
    recipe_id: int
    
    class Config:
        from_attributes = True


class RecipeBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    description: Optional[str] = None
    cuisine: Optional[str] = Field(None, max_length=100)
    servings: int = Field(default=1, gt=0)
    prep_time_minutes: Optional[int] = Field(None, gt=0)
    cook_time_minutes: Optional[int] = Field(None, gt=0)


class RecipeCreate(RecipeBase):
    ingredients: List[IngredientCreate] = []
    steps: List[StepCreate] = []


class RecipeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=200)
    description: Optional[str] = None
    cuisine: Optional[str] = Field(None, max_length=100)
    servings: Optional[int] = Field(None, gt=0)
    prep_time_minutes: Optional[int] = Field(None, gt=0)
    cook_time_minutes: Optional[int] = Field(None, gt=0)
    ingredients: Optional[List[IngredientCreate]] = None
    steps: Optional[List[StepCreate]] = None


class Recipe(RecipeBase):
    id: int
    ingredients: List[Ingredient] = []
    steps: List[Step] = []
    
    class Config:
        from_attributes = True


class PantryBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    quantity: float = Field(..., gt=0)
    unit: str = Field(..., min_length=1, max_length=50)


class PantryCreate(PantryBase):
    pass


class PantryUpdate(BaseModel):
    quantity: Optional[float] = Field(None, gt=0)
    unit: Optional[str] = Field(None, min_length=1, max_length=50)


class Pantry(PantryBase):
    id: int
    
    class Config:
        from_attributes = True


class ShoppingItem(BaseModel):
    name: str
    quantity: float
    unit: str
