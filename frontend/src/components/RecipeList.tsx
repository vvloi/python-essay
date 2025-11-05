import React, { useEffect, useState } from 'react'
import { Recipe } from '../types'

export default function RecipeList() {
  const [recipes, setRecipes] = useState<Recipe[]>([])

  useEffect(() => {
    fetch('/api/recipes')
      .then((r) => r.json())
      .then(setRecipes)
      .catch(console.error)
  }, [])

  return (
    <div className="bg-white p-4 rounded shadow">
      <h2 className="text-xl font-semibold mb-2">Recipes</h2>
      <ul>
        {recipes.map((r) => (
          <li key={r.id} className="border-b py-2">
            <div className="flex justify-between">
              <div>
                <div className="font-medium">{r.title}</div>
                <div className="text-sm text-gray-600">Serves: {r.servings}</div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
