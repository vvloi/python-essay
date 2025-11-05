import { apiClient } from './ApiClient'

export const RecipeAPI = {
  getAll: (skip = 0, limit = 100) => apiClient.get(`/recipes?skip=${skip}&limit=${limit}`),
  getById: (id: number) => apiClient.get(`/recipes/${id}`),
  search: (q: string) => apiClient.get(`/recipes/search?q=${encodeURIComponent(q)}`),
  create: (d: any) => apiClient.post('/recipes', d),
  update: (id: number, d: any) => apiClient.put(`/recipes/${id}`, d),
  delete: (id: number) => apiClient.delete(`/recipes/${id}`),
  scale: (id: number, factor: number) => apiClient.get(`/recipes/${id}/scale?factor=${factor}`),
}
