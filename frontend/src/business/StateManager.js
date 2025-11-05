class StateManager {
  constructor(){
    this.state = { recipes: [], selectedRecipe: null, pantryItems: [], shoppingList: [], selectedRecipeIds: new Set() }
    this.listeners = []
  }
  subscribe(fn){ this.listeners.push(fn); return ()=> this.listeners = this.listeners.filter(l=>l!==fn) }
  setState(upd){ this.state = {...this.state, ...upd}; this.listeners.forEach(l=>l(this.state)) }
  getState(){ return this.state }
}
export const stateManager = new StateManager()
