import { apiClient } from './ApiClient'
export const ShoppingListAPI = {
  generate: (recipeIds)=> apiClient.post('/shopping-list', recipeIds)
}
