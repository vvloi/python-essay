// Frontend 3-Layer Architecture
// Data Layer - Shopping List API

import { apiClient } from './ApiClient.js';

const ShoppingListAPI = {
    generate: (recipeIds) => apiClient.post('/shopping-list', recipeIds),
};

export { ShoppingListAPI };
