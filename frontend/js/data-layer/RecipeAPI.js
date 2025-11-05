// Frontend 3-Layer Architecture
// Data Layer - Recipe API

import { apiClient } from './ApiClient.js';

const RecipeAPI = {
    getAll: (skip = 0, limit = 100) => apiClient.get(`/recipes?skip=${skip}&limit=${limit}`),
    getById: (id) => apiClient.get(`/recipes/${id}`),
    search: (query) => apiClient.get(`/recipes/search?q=${encodeURIComponent(query)}`),
    create: (data) => apiClient.post('/recipes', data),
    update: (id, data) => apiClient.put(`/recipes/${id}`, data),
    delete: (id) => apiClient.delete(`/recipes/${id}`),
    scale: (id, factor) => apiClient.get(`/recipes/${id}/scale?factor=${factor}`),
};

export { RecipeAPI };
