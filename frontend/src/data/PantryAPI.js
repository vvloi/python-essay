import { apiClient } from './ApiClient'
export const PantryAPI = {
  getAll: ()=> apiClient.get('/pantry'),
  getById: (id)=> apiClient.get(`/pantry/${id}`),
  create: (d)=> apiClient.post('/pantry', d),
  update: (id,d)=> apiClient.put(`/pantry/${id}`, d),
  delete: (id)=> apiClient.delete(`/pantry/${id}`),
}
