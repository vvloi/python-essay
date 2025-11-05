import React from 'react'
import RecipeList from './components/RecipeList'
import Pantry from './components/Pantry'
import ShoppingList from './components/ShoppingList'

export default function App(){
  const [view, setView] = React.useState('recipes')

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-4xl mx-auto py-6 px-4 sm:px-6 lg:px-8 flex items-center justify-between">
          <h1 className="text-2xl font-bold text-gray-900">📖 Recipe Book</h1>
          <nav className="space-x-3">
            <button onClick={()=>setView('recipes')} className={`px-3 py-1 rounded ${view==='recipes'?'bg-indigo-600 text-white':'bg-gray-100'}`}>Recipes</button>
            <button onClick={()=>setView('pantry')} className={`px-3 py-1 rounded ${view==='pantry'?'bg-indigo-600 text-white':'bg-gray-100'}`}>Pantry</button>
            <button onClick={()=>setView('shopping')} className={`px-3 py-1 rounded ${view==='shopping'?'bg-indigo-600 text-white':'bg-gray-100'}`}>Shopping</button>
          </nav>
        </div>
      </header>

      <main className="max-w-4xl mx-auto py-8 px-4">
        {view === 'recipes' && <RecipeList />}
        {view === 'pantry' && <Pantry />}
        {view === 'shopping' && <ShoppingList />}
      </main>
    </div>
  )
}
