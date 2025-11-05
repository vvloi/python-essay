import { apiClient } from './ApiClient'
export const RecipeAPI = {
  getAll: (skip=0,limit=100)=> apiClient.get(`/recipes?skip=${skip}&limit=${limit}`),
  getById: (id)=> apiClient.get(`/recipes/${id}`),
  search: (q)=> apiClient.get(`/recipes/search?q=${encodeURIComponent(q)}`),
  create: (d)=> apiClient.post('/recipes', d),
  update: (id,d)=> apiClient.put(`/recipes/${id}`, d),
  delete: (id)=> apiClient.delete(`/recipes/${id}`),
  scale: (id,factor)=> apiClient.get(`/recipes/${id}/scale?factor=${factor}`)
}
