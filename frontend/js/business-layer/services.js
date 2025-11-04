// Frontend 3-Layer Architecture
// Business Layer - Services & State Management

class StateManager {
    constructor() {
        this.state = {
            recipes: [],
            selectedRecipe: null,
            pantryItems: [],
            shoppingList: [],
            selectedRecipeIds: new Set(),
        };
        this.listeners = [];
    }

    subscribe(listener) {
        this.listeners.push(listener);
        return () => {
            this.listeners = this.listeners.filter(l => l !== listener);
        };
    }

    setState(updates) {
        this.state = { ...this.state, ...updates };
        this.listeners.forEach(listener => listener(this.state));
    }

    getState() {
        return this.state;
    }
}

const stateManager = new StateManager();

// Recipe Service
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

// Pantry Service
const PantryService = {
    async loadAllPantryItems() {
        const pantryItems = await PantryAPI.getAll();
        stateManager.setState({ pantryItems });
        return pantryItems;
    },

    async createPantryItem(itemData) {
        const newItem = await PantryAPI.create(itemData);
        await this.loadAllPantryItems();
        return newItem;
    },

    async updatePantryItem(id, itemData) {
        const updatedItem = await PantryAPI.update(id, itemData);
        await this.loadAllPantryItems();
        return updatedItem;
    },

    async deletePantryItem(id) {
        await PantryAPI.delete(id);
        await this.loadAllPantryItems();
    }
};

// Shopping List Service
const ShoppingListService = {
    async generateShoppingList() {
        const { selectedRecipeIds } = stateManager.getState();
        const recipeIds = Array.from(selectedRecipeIds);
        
        if (recipeIds.length === 0) {
            throw new Error('Please select at least one recipe');
        }
        
        const shoppingList = await ShoppingListAPI.generate(recipeIds);
        stateManager.setState({ shoppingList });
        return shoppingList;
    },

    exportToText() {
        const { shoppingList } = stateManager.getState();
        if (shoppingList.length === 0) {
            return '';
        }

        let text = 'Shopping List\n';
        text += '='.repeat(40) + '\n\n';
        
        shoppingList.forEach(item => {
            text += `☐ ${item.name}: ${item.quantity} ${item.unit}\n`;
        });
        
        return text;
    },

    downloadShoppingList() {
        const text = this.exportToText();
        const blob = new Blob([text], { type: 'text/plain' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `shopping-list-${new Date().toISOString().split('T')[0]}.txt`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
    }
};
