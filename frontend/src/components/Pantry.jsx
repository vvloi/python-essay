import React from 'react'
import { PantryAPI } from '../data/PantryAPI'

export default function Pantry(){
  const [items, setItems] = React.useState([])

  React.useEffect(()=>{
    let mounted = true
    PantryAPI.getAll().then(r=>{ if(mounted) setItems(r) }).catch(()=>{})
    return ()=>{ mounted=false }
  },[])

  return (
    <div className="space-y-4">
      {items.map(it=> (
        <div key={it.id} className="bg-white shadow p-4 rounded flex justify-between">
          <div>
            <h3 className="font-medium">{it.name}</h3>
            <div className="text-sm text-gray-500">{it.quantity} {it.unit}</div>
          </div>
        </div>
      ))}
    </div>
  )
}
