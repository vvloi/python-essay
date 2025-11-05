import React, { useState } from 'react'
import RecipeList from './components/RecipeList'
import Pantry from './components/Pantry'
import ShoppingList from './components/ShoppingList'

export default function App() {
  const [activeView, setActiveView] = useState<'recipes' | 'pantry' | 'shopping'>('recipes')
  const [selectedRecipeIds, setSelectedRecipeIds] = useState<Set<number>>(new Set())
  const [sidebarOpen, setSidebarOpen] = useState(false)
  
  // Filter states
  const [selectedCuisines, setSelectedCuisines] = useState<Set<string>>(new Set())
  const [selectedTimeRange, setSelectedTimeRange] = useState<string | null>(null)

  const handleToggleRecipe = (id: number) => {
    const newSet = new Set(selectedRecipeIds)
    if (newSet.has(id)) {
      newSet.delete(id)
    } else {
      newSet.add(id)
    }
    setSelectedRecipeIds(newSet)
  }

  const handleToggleCuisine = (cuisine: string) => {
    setSelectedCuisines((prev) => {
      const newSet = new Set(prev)
      if (newSet.has(cuisine)) {
        newSet.delete(cuisine)
      } else {
        newSet.add(cuisine)
      }
      return newSet
    })
  }

  const handleClearFilters = () => {
    setSelectedCuisines(new Set())
    setSelectedTimeRange(null)
  }

  return (
    <div className="min-h-screen bg-gray-100">
      {/* Navbar */}
      <nav className="bg-white shadow-md sticky top-0 z-40">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between h-16">
            <div className="flex items-center space-x-4">
              <button
                onClick={() => setSidebarOpen(!sidebarOpen)}
                className="lg:hidden text-gray-700 hover:text-indigo-600 transition"
              >
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 6h16M4 12h16M4 18h16" />
                </svg>
              </button>
              <span className="text-2xl font-bold text-indigo-600">🍳 Recipe Book</span>
            </div>
            <div className="flex items-center space-x-2 sm:space-x-4">
              <button
                onClick={() => setActiveView('recipes')}
                className={`px-3 sm:px-4 py-2 rounded-lg font-medium transition text-sm sm:text-base ${
                  activeView === 'recipes'
                    ? 'bg-indigo-600 text-white'
                    : 'text-gray-700 hover:bg-gray-100'
                }`}
              >
                <span className="hidden sm:inline">📖 Recipes</span>
                <span className="sm:hidden">📖</span>
              </button>
              <button
                onClick={() => setActiveView('pantry')}
                className={`px-3 sm:px-4 py-2 rounded-lg font-medium transition text-sm sm:text-base ${
                  activeView === 'pantry'
                    ? 'bg-indigo-600 text-white'
                    : 'text-gray-700 hover:bg-gray-100'
                }`}
              >
                <span className="hidden sm:inline">🥫 Pantry</span>
                <span className="sm:hidden">🥫</span>
              </button>
              <button
                onClick={() => setActiveView('shopping')}
                className={`px-3 sm:px-4 py-2 rounded-lg font-medium transition relative text-sm sm:text-base ${
                  activeView === 'shopping'
                    ? 'bg-indigo-600 text-white'
                    : 'text-gray-700 hover:bg-gray-100'
                }`}
              >
                <span className="hidden sm:inline">🛒 Shopping List</span>
                <span className="sm:hidden">🛒</span>
                {selectedRecipeIds.size > 0 && (
                  <span className="absolute -top-1 -right-1 bg-red-500 text-white text-xs rounded-full w-5 h-5 flex items-center justify-center">
                    {selectedRecipeIds.size}
                  </span>
                )}
              </button>
            </div>
          </div>
        </div>
      </nav>

      <div className="flex">
        {/* Sidebar - only show on recipes view */}
        {activeView === 'recipes' && (
          <>
            {/* Mobile sidebar overlay */}
            {sidebarOpen && (
              <div
                className="fixed inset-0 bg-black bg-opacity-50 z-30 lg:hidden"
                onClick={() => setSidebarOpen(false)}
              />
            )}
            
            {/* Sidebar */}
            <aside
              className={`fixed lg:sticky top-16 left-0 h-[calc(100vh-4rem)] bg-white shadow-lg z-30 transition-transform duration-300 lg:translate-x-0 ${
                sidebarOpen ? 'translate-x-0' : '-translate-x-full'
              } w-64 overflow-y-auto`}
            >
              <div className="p-6">
                <div className="mb-6">
                  <h3 className="text-lg font-bold text-gray-900 mb-2">🎯 Quick Actions</h3>
                  <div className="space-y-2">
                    <button className="w-full px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition font-medium text-sm">
                      ➕ Add Recipe
                    </button>
                    <button className="w-full px-4 py-2 bg-indigo-600 text-white rounded-lg hover:bg-indigo-700 transition font-medium text-sm">
                      📥 Import Recipe
                    </button>
                  </div>
                </div>

                <div className="mb-6">
                  <div className="flex items-center justify-between mb-3">
                    <h3 className="text-lg font-bold text-gray-900">🏷️ Filter by Cuisine</h3>
                    {(selectedCuisines.size > 0 || selectedTimeRange) && (
                      <button
                        onClick={handleClearFilters}
                        className="text-xs text-red-600 hover:text-red-700 font-medium"
                      >
                        Clear
                      </button>
                    )}
                  </div>
                  <div className="space-y-2">
                    {['Vietnamese', 'Italian', 'Mexican', 'Japanese', 'Thai'].map((cuisine) => (
                      <label key={cuisine} className="flex items-center text-sm cursor-pointer hover:bg-gray-50 p-1 rounded">
                        <input
                          type="checkbox"
                          checked={selectedCuisines.has(cuisine)}
                          onChange={() => handleToggleCuisine(cuisine)}
                          className="mr-2 rounded text-indigo-600"
                        />
                        <span>{cuisine}</span>
                      </label>
                    ))}
                  </div>
                </div>

                <div className="mb-6">
                  <h3 className="text-lg font-bold text-gray-900 mb-3">⏱️ Cooking Time</h3>
                  <div className="space-y-2">
                    <label className="flex items-center text-sm cursor-pointer hover:bg-gray-50 p-1 rounded">
                      <input
                        type="radio"
                        name="time"
                        checked={selectedTimeRange === 'short'}
                        onChange={() => setSelectedTimeRange('short')}
                        className="mr-2 text-indigo-600"
                      />
                      <span>&lt; 30 min</span>
                    </label>
                    <label className="flex items-center text-sm cursor-pointer hover:bg-gray-50 p-1 rounded">
                      <input
                        type="radio"
                        name="time"
                        checked={selectedTimeRange === 'medium'}
                        onChange={() => setSelectedTimeRange('medium')}
                        className="mr-2 text-indigo-600"
                      />
                      <span>30-60 min</span>
                    </label>
                    <label className="flex items-center text-sm cursor-pointer hover:bg-gray-50 p-1 rounded">
                      <input
                        type="radio"
                        name="time"
                        checked={selectedTimeRange === 'long'}
                        onChange={() => setSelectedTimeRange('long')}
                        className="mr-2 text-indigo-600"
                      />
                      <span>&gt; 60 min</span>
                    </label>
                    <label className="flex items-center text-sm cursor-pointer hover:bg-gray-50 p-1 rounded">
                      <input
                        type="radio"
                        name="time"
                        checked={selectedTimeRange === null}
                        onChange={() => setSelectedTimeRange(null)}
                        className="mr-2 text-indigo-600"
                      />
                      <span>All</span>
                    </label>
                  </div>
                </div>

                <div>
                  <h3 className="text-lg font-bold text-gray-900 mb-3">📊 Stats</h3>
                  <div className="bg-gray-50 rounded-lg p-3 space-y-1 text-sm">
                    <div className="flex justify-between">
                      <span className="text-gray-600">Total Recipes:</span>
                      <span className="font-bold">3</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-gray-600">Pantry Items:</span>
                      <span className="font-bold">7</span>
                    </div>
                    <div className="flex justify-between">
                      <span className="text-gray-600">Selected:</span>
                      <span className="font-bold text-indigo-600">{selectedRecipeIds.size}</span>
                    </div>
                  </div>
                </div>
              </div>
            </aside>
          </>
        )}

        {/* Main Content */}
        <main className="flex-1 p-4 sm:p-6 lg:p-8">
          <div className="max-w-7xl mx-auto">
            {activeView === 'recipes' && (
              <RecipeList 
                selectedRecipeIds={selectedRecipeIds}
                onToggleRecipe={handleToggleRecipe}
                cuisineFilters={selectedCuisines}
                timeRangeFilter={selectedTimeRange}
              />
            )}
            {activeView === 'pantry' && <Pantry />}
            {activeView === 'shopping' && (
              <ShoppingList 
                selectedRecipeIds={selectedRecipeIds}
                onClearSelection={() => setSelectedRecipeIds(new Set())}
              />
            )}
          </div>
        </main>
      </div>
    </div>
  )
}
