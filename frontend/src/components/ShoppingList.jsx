import React from 'react'
import { ShoppingListAPI } from '../data/ShoppingListAPI'
import { stateManager } from '../business/StateManager'

export default function ShoppingList(){
  const [list, setList] = React.useState([])

  React.useEffect(()=>{
    const state = stateManager.getState()
    setList(state.shoppingList || [])
    const unsub = stateManager.subscribe(s=> setList(s.shoppingList || []))
    return ()=> unsub()
  },[])

  return (
    <div>
      {list.length===0 ? <div className="text-gray-500">No items. Select recipes and generate a list.</div> : (
        <ul className="space-y-2">
          {list.map((it,idx)=> <li key={idx} className="bg-white p-3 rounded shadow">{it.name} — {it.quantity} {it.unit}</li>)}
        </ul>
      )}
    </div>
  )
}
