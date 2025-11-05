const API_BASE_URL = '/api'

class ApiClient {
  async request(endpoint: string, options: RequestInit = {}){
    const url = `${API_BASE_URL}${endpoint}`
    const config: RequestInit = { headers: {'Content-Type':'application/json'}, ...options }
    const res = await fetch(url, config)
    if(!res.ok){
      const err = await res.json().catch(()=> ({detail: 'Request failed'}))
      throw new Error((err && (err as any).detail) || `HTTP ${res.status}`)
    }
    if(res.status===204) return null
    return res.json()
  }
  get(e: string){ return this.request(e, {method:'GET'}) }
  post(e: string, d?: any){ return this.request(e, {method:'POST', body: JSON.stringify(d)}) }
  put(e: string, d?: any){ return this.request(e, {method:'PUT', body: JSON.stringify(d)}) }
  delete(e: string){ return this.request(e, {method:'DELETE'}) }
}

export const apiClient = new ApiClient()
