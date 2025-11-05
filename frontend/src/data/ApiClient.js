const API_BASE_URL = '/api'

class ApiClient {
  async request(endpoint, options = {}){
    const url = `${API_BASE_URL}${endpoint}`
    const config = { headers: {'Content-Type':'application/json'}, ...options }
    const res = await fetch(url, config)
    if(!res.ok){
      const err = await res.json().catch(()=> ({detail: 'Request failed'}))
      throw new Error(err.detail || `HTTP ${res.status}`)
    }
    if(res.status===204) return null
    return res.json()
  }
  get(e){ return this.request(e, {method:'GET'}) }
  post(e,d){ return this.request(e, {method:'POST', body: JSON.stringify(d)}) }
  put(e,d){ return this.request(e, {method:'PUT', body: JSON.stringify(d)}) }
  delete(e){ return this.request(e, {method:'DELETE'}) }
}

export const apiClient = new ApiClient()
