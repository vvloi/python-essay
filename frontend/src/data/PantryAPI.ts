import { apiClient } from './ApiClient'
export const PantryAPI = {
  getAll: () => apiClient.get('/pantry'),
  getById: (id: number) => apiClient.get(`/pantry/${id}`),
  create: (d: any) => apiClient.post('/pantry', d),
  update: (id: number, d: any) => apiClient.put(`/pantry/${id}`, d),
  delete: (id: number) => apiClient.delete(`/pantry/${id}`),
}
