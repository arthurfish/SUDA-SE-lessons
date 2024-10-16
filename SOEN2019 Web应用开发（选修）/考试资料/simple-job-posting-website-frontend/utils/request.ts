import axios from 'axios'
import { getToken, setToken } from './auth'

const request = axios.create({
  baseURL: 'http://localhost:8080',
  timeout: 5000,
  headers: {
    'Content-Type': 'application/json;charset=UTF-8'
  }
})

request.interceptors.request.use(
  config => {
    const token = getToken()
    if (token !== null && token !== '' && config.url !== '/login') {
      if (config.headers == null) config.headers = {}
      if (typeof config.headers.set === 'function') {
        config.headers.set('Authorization', `Bearer ${token}`)
      }
    }
    return config
  },
  async error => {
    return await Promise.reject(error)
  }
)

request.interceptors.response.use(
  res => {
    const token = res.headers.Authorization
    if (token != null) {
      setToken(token)
    }
    return res.data
  },
  async error => {
    return await Promise.reject(error)
  }
)

export default request
