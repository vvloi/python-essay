export interface Ingredient { id?: number; recipe_id?: number; name: string; quantity: number; unit: string }
export interface Step { id?: number; recipe_id?: number; step_number: number; instruction: string }
export interface Recipe { id: number; name: string; description?: string; cuisine?: string; servings: number; prep_time_minutes?: number; cook_time_minutes?: number; ingredients?: Ingredient[]; steps?: Step[] }
export interface PantryItem { id: number; name: string; quantity: number; unit: string }
export interface ShoppingItem { name: string; quantity: number; unit: string }
