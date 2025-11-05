// Frontend 3-Layer Architecture
// Business Layer - Shopping List Service

import { ShoppingListAPI } from '../data-layer/ShoppingListAPI.js';
import { stateManager } from './StateManager.js';

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

export { ShoppingListService };
