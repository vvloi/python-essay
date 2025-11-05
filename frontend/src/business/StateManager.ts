type Listener = (s: any) => void

class StateManager {
  state: any
  listeners: Listener[]
  constructor(){
    this.state = { recipes: [], selectedRecipe: null, pantryItems: [], shoppingList: [], selectedRecipeIds: new Set<number>() }
    this.listeners = []
  }
  subscribe(fn: Listener){ this.listeners.push(fn); return ()=> this.listeners = this.listeners.filter(l=>l!==fn) }
  setState(upd: any){ this.state = {...this.state, ...upd}; this.listeners.forEach(l=>l(this.state)) }
  getState(){ return this.state }
}
export const stateManager = new StateManager()
