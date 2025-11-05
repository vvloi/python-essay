import { apiClient } from './ApiClient'
export const ShoppingListAPI = {
  generate: (recipeIds: number[]) => apiClient.post('/shopping-list', recipeIds),
}
