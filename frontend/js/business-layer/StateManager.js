// Frontend 3-Layer Architecture
// Business Layer - State Management

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

export { stateManager };
