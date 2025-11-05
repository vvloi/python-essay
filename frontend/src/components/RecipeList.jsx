import React from 'react'
import { RecipeAPI } from '../data/RecipeAPI'

export default function RecipeList(){
  const [recipes, setRecipes] = React.useState([])
  const [loading, setLoading] = React.useState(true)

  React.useEffect(()=>{
    let mounted = true
    RecipeAPI.getAll().then(r=>{ if(mounted){ setRecipes(r); setLoading(false) } }).catch(()=>setLoading(false))
    return ()=>{ mounted=false }
  },[])

  if(loading) return <div>Loading...</div>
  return (
    <div className="space-y-4">
      {recipes.map(r=> (
        <div key={r.id} className="bg-white shadow p-4 rounded">
          <div className="flex justify-between items-start">
            <div>
              <h2 className="text-lg font-semibold">{r.name}</h2>
              <p className="text-sm text-gray-500">{r.cuisine}</p>
            </div>
            <div className="text-sm text-gray-600">{r.servings} servings</div>
          </div>
          {r.description && <p className="mt-2 text-gray-700">{r.description}</p>}
        </div>
      ))}
    </div>
  )
}
