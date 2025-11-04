// Frontend 3-Layer Architecture
// Data Layer - Pantry API

import { apiClient } from './ApiClient.js';

const PantryAPI = {
    getAll: () => apiClient.get('/pantry'),
    getById: (id) => apiClient.get(`/pantry/${id}`),
    create: (data) => apiClient.post('/pantry', data),
    update: (id, data) => apiClient.put(`/pantry/${id}`, data),
    delete: (id) => apiClient.delete(`/pantry/${id}`),
};

export { PantryAPI };
