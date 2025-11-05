import React, { useEffect, useState } from 'react'
import { PantryItem } from '../types'

export default function Pantry() {
  const [items, setItems] = useState<PantryItem[]>([])

  useEffect(() => {
    fetch('/api/pantry')
      .then((r) => r.json())
      .then(setItems)
      .catch(console.error)
  }, [])

  return (
    <div className="bg-white p-4 rounded shadow mb-4">
      <h2 className="text-xl font-semibold mb-2">Pantry</h2>
      <ul>
        {items.map((it) => (
          <li key={it.id} className="border-b py-2">
            <div className="flex justify-between">
              <div>
                <div className="font-medium">{it.name}</div>
                <div className="text-sm text-gray-600">{it.quantity} {it.unit}</div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
