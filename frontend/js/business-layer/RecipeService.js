// Frontend 3-Layer Architecture
// Business Layer - Recipe Service

import { RecipeAPI } from '../data-layer/RecipeAPI.js';
import { stateManager } from './StateManager.js';

const RecipeService = {
    async loadAllRecipes() {
        const recipes = await RecipeAPI.getAll();
        stateManager.setState({ recipes });
        return recipes;
    },

    async searchRecipes(query) {
        if (!query.trim()) {
            return await this.loadAllRecipes();
        }
        const recipes = await RecipeAPI.search(query);
        stateManager.setState({ recipes });
        return recipes;
    },

    async getRecipeDetails(id) {
        const recipe = await RecipeAPI.getById(id);
        stateManager.setState({ selectedRecipe: recipe });
        return recipe;
    },

    async createRecipe(recipeData) {
        const newRecipe = await RecipeAPI.create(recipeData);
        await this.loadAllRecipes();
        return newRecipe;
    },

    async updateRecipe(id, recipeData) {
        const updatedRecipe = await RecipeAPI.update(id, recipeData);
        await this.loadAllRecipes();
        return updatedRecipe;
    },

    async deleteRecipe(id) {
        await RecipeAPI.delete(id);
        const { selectedRecipeIds } = stateManager.getState();
        selectedRecipeIds.delete(id);
        stateManager.setState({ selectedRecipeIds });
        await this.loadAllRecipes();
    },

    async scaleRecipe(id, factor) {
        return await RecipeAPI.scale(id, factor);
    },

    toggleRecipeSelection(id) {
        const { selectedRecipeIds } = stateManager.getState();
        if (selectedRecipeIds.has(id)) {
            selectedRecipeIds.delete(id);
        } else {
            selectedRecipeIds.add(id);
        }
        stateManager.setState({ selectedRecipeIds: new Set(selectedRecipeIds) });
    },

    clearRecipeSelection() {
        stateManager.setState({ selectedRecipeIds: new Set() });
    }
};

export { RecipeService };
