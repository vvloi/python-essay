import React, { useEffect, useState } from 'react'
import { Recipe } from '../types'

interface RecipeListProps {
  selectedRecipeIds: Set<number>
  onToggleRecipe: (id: number) => void
  cuisineFilters: Set<string>
  timeRangeFilter: string | null
}

export default function RecipeList({ 
  selectedRecipeIds, 
  onToggleRecipe,
  cuisineFilters,
  timeRangeFilter
}: RecipeListProps) {
  const [recipes, setRecipes] = useState<Recipe[]>([])
  const [selectedRecipe, setSelectedRecipe] = useState<Recipe | null>(null)
  const [searchQuery, setSearchQuery] = useState('')

  useEffect(() => {
    fetch('/api/recipes')
      .then((r) => r.json())
      .then(setRecipes)
      .catch(console.error)
  }, [])

  const filteredRecipes = recipes.filter((r) => {
    // Search filter
    const matchesSearch = r.name.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (r.cuisine && r.cuisine.toLowerCase().includes(searchQuery.toLowerCase()))
    
    if (!matchesSearch) return false

    // Cuisine filter
    if (cuisineFilters.size > 0) {
      if (!r.cuisine || !cuisineFilters.has(r.cuisine)) {
        return false
      }
    }

    // Time range filter
    if (timeRangeFilter) {
      const totalTime = (r.prep_time_minutes || 0) + (r.cook_time_minutes || 0)
      
      if (timeRangeFilter === 'short' && totalTime >= 30) return false
      if (timeRangeFilter === 'medium' && (totalTime < 30 || totalTime > 60)) return false
      if (timeRangeFilter === 'long' && totalTime <= 60) return false
    }

    return true
  })

  // Beautiful recipe images
  const getRecipeImage = (name: string) => {
    // Vietnamese
    if (name.includes('Phở')) return 'https://images.unsplash.com/photo-1626082927389-6cd097cdc6ec?w=500&h=400&fit=crop'
    if (name.includes('Bún Chả')) return 'https://images.unsplash.com/photo-1559314809-0d155014e29e?w=500&h=400&fit=crop'
    if (name.includes('Bánh Mì')) return 'https://images.unsplash.com/photo-1623428187969-5da2dcea5ebf?w=500&h=400&fit=crop'
    if (name.includes('Cơm Tấm')) return 'https://images.unsplash.com/photo-1585032226651-759b368d7246?w=500&h=400&fit=crop'
    if (name.includes('Gỏi Cuốn')) return 'https://images.unsplash.com/photo-1594041680638-bbe2706f3a88?w=500&h=400&fit=crop'
    if (name.includes('Bún Bò Huế')) return 'https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=500&h=400&fit=crop'
    
    // Italian
    if (name.includes('Carbonara')) return 'https://images.unsplash.com/photo-1612874742237-6526221588e3?w=500&h=400&fit=crop'
    if (name.includes('Pizza')) return 'https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500&h=400&fit=crop'
    if (name.includes('Tiramisu')) return 'https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=500&h=400&fit=crop'
    
    // Japanese
    if (name.includes('Sushi')) return 'https://images.unsplash.com/photo-1579584425555-c3ce17fd4351?w=500&h=400&fit=crop'
    if (name.includes('Ramen')) return 'https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=500&h=400&fit=crop'
    
    // Thai
    if (name.includes('Pad Thai')) return 'https://images.unsplash.com/photo-1559314809-0d155014e29e?w=500&h=400&fit=crop'
    if (name.includes('Tom Yum')) return 'https://images.unsplash.com/photo-1569562211093-4ed0d0758f12?w=500&h=400&fit=crop'
    
    // Mexican
    if (name.includes('Tacos')) return 'https://images.unsplash.com/photo-1565299507177-b0ac66763828?w=500&h=400&fit=crop'
    if (name.includes('Guacamole')) return 'https://images.unsplash.com/photo-1604467794349-0b74285de7e7?w=500&h=400&fit=crop'
    
    // Default
    return 'https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=500&h=400&fit=crop'
  }

  const activeFiltersCount = cuisineFilters.size + (timeRangeFilter ? 1 : 0)

  return (
    <div>
      {/* Search bar */}
      <div className="mb-6">
        <input
          type="text"
          placeholder="🔍 Search recipes by name or cuisine..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-indigo-500 focus:border-transparent"
        />
      </div>

      {/* Filter badges and results count */}
      <div className="mb-4 flex items-center justify-between">
        <div className="flex items-center gap-2 flex-wrap">
          {activeFiltersCount > 0 && (
            <span className="text-sm text-gray-600">
              🔍 {activeFiltersCount} filter{activeFiltersCount > 1 ? 's' : ''} active
            </span>
          )}
          {Array.from(cuisineFilters).map((cuisine) => (
            <span key={cuisine} className="px-2 py-1 bg-indigo-100 text-indigo-700 rounded-full text-xs font-medium">
              {cuisine}
            </span>
          ))}
          {timeRangeFilter && (
            <span className="px-2 py-1 bg-green-100 text-green-700 rounded-full text-xs font-medium">
              {timeRangeFilter === 'short' ? '< 30 min' : timeRangeFilter === 'medium' ? '30-60 min' : '> 60 min'}
            </span>
          )}
        </div>
        <span className="text-sm text-gray-600">
          {filteredRecipes.length} recipe{filteredRecipes.length !== 1 ? 's' : ''} found
        </span>
      </div>

      {/* Recipe Grid */}
      {filteredRecipes.length === 0 ? (
        <div className="text-center py-12">
          <div className="text-6xl mb-4">🔍</div>
          <h3 className="text-xl font-bold text-gray-900 mb-2">No recipes found</h3>
          <p className="text-gray-600">Try adjusting your filters or search query</p>
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {filteredRecipes.map((recipe) => (
            <div
              key={recipe.id}
              className="bg-white rounded-lg shadow-md overflow-hidden hover:shadow-xl transition cursor-pointer"
              onClick={() => setSelectedRecipe(recipe)}
            >
            {/* Recipe Image */}
            <div className="relative h-48 bg-gray-200">
              <img
                src={getRecipeImage(recipe.name)}
                alt={recipe.name}
                className="w-full h-full object-cover"
              />
              {/* Checkbox for shopping list */}
              <div className="absolute top-2 right-2">
                <input
                  type="checkbox"
                  checked={selectedRecipeIds.has(recipe.id)}
                  onChange={(e) => {
                    e.stopPropagation()
                    onToggleRecipe(recipe.id)
                  }}
                  className="w-5 h-5 text-indigo-600 rounded focus:ring-indigo-500 cursor-pointer"
                />
              </div>
            </div>

            {/* Recipe Info */}
            <div className="p-4">
              <h3 className="text-lg font-bold text-gray-900 mb-2">
                {recipe.name}
              </h3>
              <div className="flex items-center text-sm text-gray-600 space-x-2">
                {recipe.cuisine && (
                  <span className="px-2 py-1 bg-indigo-100 text-indigo-700 rounded">
                    {recipe.cuisine}
                  </span>
                )}
                <span>👥 {recipe.servings} servings</span>
              </div>
              {recipe.description && (
                <p className="mt-2 text-sm text-gray-600 line-clamp-2">{recipe.description}</p>
              )}
              <div className="mt-3 flex items-center justify-between text-xs text-gray-500">
                {recipe.prep_time_minutes && <span>⏱️ Prep: {recipe.prep_time_minutes}m</span>}
                {recipe.cook_time_minutes && <span>🍳 Cook: {recipe.cook_time_minutes}m</span>}
              </div>
            </div>
          </div>
          ))}
        </div>
      )}

      {/* Detail Modal */}
      {selectedRecipe && (
        <div
          className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4"
          onClick={() => setSelectedRecipe(null)}
        >
          <div
            className="bg-white rounded-lg max-w-3xl w-full max-h-[90vh] overflow-y-auto"
            onClick={(e) => e.stopPropagation()}
          >
            {/* Modal Header */}
            <div className="sticky top-0 bg-white border-b px-6 py-4 flex justify-between items-center">
              <h2 className="text-2xl font-bold text-gray-900">{selectedRecipe.name}</h2>
              <button
                onClick={() => setSelectedRecipe(null)}
                className="text-gray-500 hover:text-gray-700 text-2xl"
              >
                ×
              </button>
            </div>

            {/* Modal Content */}
            <div className="p-6">
              {/* Image */}
              <img
                src={getRecipeImage(selectedRecipe.name)}
                alt={selectedRecipe.name}
                className="w-full h-64 object-cover rounded-lg mb-4"
              />

              {/* Meta Info */}
              <div className="flex flex-wrap gap-3 mb-4">
                {selectedRecipe.cuisine && (
                  <span className="px-3 py-1 bg-indigo-100 text-indigo-700 rounded-full text-sm">
                    {selectedRecipe.cuisine}
                  </span>
                )}
                <span className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm">
                  👥 {selectedRecipe.servings} servings
                </span>
                {selectedRecipe.prep_time_minutes && (
                  <span className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm">
                    ⏱️ {selectedRecipe.prep_time_minutes} min prep
                  </span>
                )}
                {selectedRecipe.cook_time_minutes && (
                  <span className="px-3 py-1 bg-gray-100 text-gray-700 rounded-full text-sm">
                    🍳 {selectedRecipe.cook_time_minutes} min cook
                  </span>
                )}
              </div>

              {/* Description */}
              {selectedRecipe.description && (
                <p className="text-gray-700 mb-6">{selectedRecipe.description}</p>
              )}

              {/* Ingredients */}
              {selectedRecipe.ingredients && selectedRecipe.ingredients.length > 0 && (
                <div className="mb-6">
                  <h3 className="text-lg font-bold text-gray-900 mb-3">🥘 Ingredients</h3>
                  <ul className="space-y-2">
                    {selectedRecipe.ingredients.map((ing, idx) => (
                      <li key={idx} className="flex items-center text-gray-700">
                        <span className="w-2 h-2 bg-indigo-600 rounded-full mr-3"></span>
                        <span>
                          {ing.name}: {ing.quantity} {ing.unit}
                        </span>
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* Steps */}
              {selectedRecipe.steps && selectedRecipe.steps.length > 0 && (
                <div>
                  <h3 className="text-lg font-bold text-gray-900 mb-3">📝 Instructions</h3>
                  <ol className="space-y-3">
                    {selectedRecipe.steps.map((step, idx) => (
                      <li key={idx} className="flex">
                        <span className="flex-shrink-0 w-8 h-8 bg-indigo-600 text-white rounded-full flex items-center justify-center font-bold mr-3">
                          {step.step_number}
                        </span>
                        <p className="text-gray-700 pt-1">{step.instruction}</p>
                      </li>
                    ))}
                  </ol>
                </div>
              )}

              {/* Action Buttons */}
              <div className="mt-6 flex gap-3">
                <button
                  onClick={() => {
                    onToggleRecipe(selectedRecipe.id)
                  }}
                  className={`flex-1 py-2 px-4 rounded-lg font-medium transition ${
                    selectedRecipeIds.has(selectedRecipe.id)
                      ? 'bg-red-600 text-white hover:bg-red-700'
                      : 'bg-indigo-600 text-white hover:bg-indigo-700'
                  }`}
                >
                  {selectedRecipeIds.has(selectedRecipe.id) ? '✓ Added to Shopping List' : '🛒 Add to Shopping List'}
                </button>
              </div>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}
