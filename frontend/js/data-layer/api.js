// Frontend 3-Layer Architecture
// Data Layer - API Communication

const API_BASE_URL = '/api';

class ApiClient {
    async request(endpoint, options = {}) {
        const url = `${API_BASE_URL}${endpoint}`;
        const config = {
            headers: {
                'Content-Type': 'application/json',
                ...options.headers,
            },
            ...options,
        };

        const response = await fetch(url, config);
        
        if (!response.ok) {
            const error = await response.json().catch(() => ({ detail: 'Request failed' }));
            throw new Error(error.detail || `HTTP ${response.status}`);
        }
        
        if (response.status === 204) {
            return null;
        }
        
        return await response.json();
    }

    get(endpoint) {
        return this.request(endpoint, { method: 'GET' });
    }

    post(endpoint, data) {
        return this.request(endpoint, {
            method: 'POST',
            body: JSON.stringify(data),
        });
    }

    put(endpoint, data) {
        return this.request(endpoint, {
            method: 'PUT',
            body: JSON.stringify(data),
        });
    }

    delete(endpoint) {
        return this.request(endpoint, { method: 'DELETE' });
    }
}

const apiClient = new ApiClient();

// Recipe API
const RecipeAPI = {
    getAll: (skip = 0, limit = 100) => apiClient.get(`/recipes?skip=${skip}&limit=${limit}`),
    getById: (id) => apiClient.get(`/recipes/${id}`),
    search: (query) => apiClient.get(`/recipes/search?q=${encodeURIComponent(query)}`),
    create: (data) => apiClient.post('/recipes', data),
    update: (id, data) => apiClient.put(`/recipes/${id}`, data),
    delete: (id) => apiClient.delete(`/recipes/${id}`),
    scale: (id, factor) => apiClient.get(`/recipes/${id}/scale?factor=${factor}`),
};

// Pantry API
const PantryAPI = {
    getAll: () => apiClient.get('/pantry'),
    getById: (id) => apiClient.get(`/pantry/${id}`),
    create: (data) => apiClient.post('/pantry', data),
    update: (id, data) => apiClient.put(`/pantry/${id}`, data),
    delete: (id) => apiClient.delete(`/pantry/${id}`),
};

// Shopping List API
const ShoppingListAPI = {
    generate: (recipeIds) => apiClient.post('/shopping-list', recipeIds),
};
