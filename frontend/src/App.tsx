import React from 'react'
import RecipeList from './components/RecipeList'
import Pantry from './components/Pantry'
import ShoppingList from './components/ShoppingList'

export default function App() {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-6">Recipe Book</h1>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
          <div className="md:col-span-2">
            <RecipeList />
          </div>
          <div className="">
            <Pantry />
            <ShoppingList />
          </div>
        </div>
      </div>
    </div>
  )
}
