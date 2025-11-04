// Frontend 3-Layer Architecture
// Business Layer - Pantry Service

import { PantryAPI } from '../data-layer/PantryAPI.js';
import { stateManager } from './StateManager.js';

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

export { PantryService };
