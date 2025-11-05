import React, { useEffect, useState } from 'react'

interface ShoppingListProps {
  selectedRecipeIds: Set<number>
  onClearSelection: () => void
}

interface ShoppingItem {
  name: string
  quantity: number
  unit: string
}

export default function ShoppingList({ selectedRecipeIds, onClearSelection }: ShoppingListProps) {
  const [shoppingItems, setShoppingItems] = useState<ShoppingItem[]>([])
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    if (selectedRecipeIds.size === 0) {
      setShoppingItems([])
      return
    }

    setLoading(true)
    setError(null)

    const recipeIds = Array.from(selectedRecipeIds)

    fetch('/api/shopping-list', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(recipeIds),
    })
      .then((res) => {
        if (!res.ok) throw new Error('Failed to generate shopping list')
        return res.json()
      })
      .then((data) => {
        setShoppingItems(data || [])
        setLoading(false)
      })
      .catch((err) => {
        setError(err.message)
        setLoading(false)
      })
  }, [selectedRecipeIds])

  const handleExport = () => {
    const text = shoppingItems
      .map((item) => `${item.name}: ${item.quantity} ${item.unit}`)
      .join('\n')
    
    const blob = new Blob([text], { type: 'text/plain' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'shopping-list.txt'
    a.click()
    URL.revokeObjectURL(url)
  }

  if (selectedRecipeIds.size === 0) {
    return (
      <div className="bg-white p-8 rounded-lg shadow text-center">
        <div className="text-6xl mb-4">🛒</div>
        <h2 className="text-2xl font-bold text-gray-900 mb-2">Your Shopping List is Empty</h2>
        <p className="text-gray-600">
          Select recipes by checking the boxes on recipe cards to generate your shopping list!
        </p>
      </div>
    )
  }

  if (loading) {
    return (
      <div className="bg-white p-8 rounded-lg shadow text-center">
        <div className="text-4xl mb-4">⏳</div>
        <p className="text-gray-600">Generating your shopping list...</p>
      </div>
    )
  }

  if (error) {
    return (
      <div className="bg-white p-8 rounded-lg shadow text-center">
        <div className="text-4xl mb-4">⚠️</div>
        <h2 className="text-xl font-bold text-red-600 mb-2">Error</h2>
        <p className="text-gray-600">{error}</p>
      </div>
    )
  }

  return (
    <div className="bg-white rounded-lg shadow">
      {/* Header */}
      <div className="border-b px-6 py-4 flex justify-between items-center">
        <div>
          <h2 className="text-2xl font-bold text-gray-900">Shopping List</h2>
          <p className="text-sm text-gray-600 mt-1">
            {selectedRecipeIds.size} recipe{selectedRecipeIds.size > 1 ? 's' : ''} selected
          </p>
        </div>
        <div className="flex gap-3">
          <button
            onClick={handleExport}
            className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition font-medium"
          >
            📥 Export
          </button>
          <button
            onClick={onClearSelection}
            className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition font-medium"
          >
            🗑️ Clear All
          </button>
        </div>
      </div>

      {/* Shopping Items */}
      <div className="p-6">
        {shoppingItems.length === 0 ? (
          <p className="text-gray-600 text-center py-8">
            All ingredients are already in your pantry! 🎉
          </p>
        ) : (
          <ul className="space-y-3">
            {shoppingItems.map((item, idx) => (
              <li
                key={idx}
                className="flex items-center justify-between p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition"
              >
                <div className="flex items-center">
                  <span className="w-8 h-8 bg-indigo-600 text-white rounded-full flex items-center justify-center font-bold mr-4">
                    {idx + 1}
                  </span>
                  <span className="font-medium text-gray-900">{item.name}</span>
                </div>
                <span className="text-gray-600 font-medium">
                  {item.quantity} {item.unit}
                </span>
              </li>
            ))}
          </ul>
        )}
      </div>

      {/* Footer Stats */}
      <div className="border-t px-6 py-4 bg-gray-50 rounded-b-lg">
        <p className="text-sm text-gray-600">
          📦 Total items to buy: <span className="font-bold text-gray-900">{shoppingItems.length}</span>
        </p>
      </div>
    </div>
  )
}
