// use this file when starting with http request
import router from '../router/index'
import axios from 'axios'
// import store from 'src/store'
const http: any = axios.create({
  timeout: 5000,
  baseURL: `${process.env.http_base_url}`,
  headers: { 'content-type': 'application/x-www-form-urlencoded' },
  withCredentials: true
})

// http interceptor for response
http.interceptors.response.use((response: { [x: string]: any; status: number; data: any; }) => {
  if (response.status !== 200) {
    return Promise.reject(new Error('request failed'))
  }

  const result = response.data
  // cookie过期则跳转至登录页面
  if (result.code === 'login') {
    if (result.data) {
      if (result.data.login_url) {
        let arrUrl = window.location.href.split('//')
        let firUrl = arrUrl[1].split('#')
        let oriUrl = firUrl[0].split('/')
        if (oriUrl.length > 3) {
          let href = router.resolve({
            path: '/login',
            query: { path: window.location.href, appId: result.data.app_id, org: oriUrl[1] }
          })
          top.location.href = 'http://' + oriUrl[0] + '/' + oriUrl[1] + '/' + 'auth/' + href.href
        } else {
          let href = router.resolve({
            path: '/login',
            query: { path: window.location.href, appId: result.data.app_id, org: '' }
          })
          top.location.href = result.data.login_url + '/' + 'auth/' + href.href
        }
      } else {
        router.push('/404')
      }
    } else {
      router.push('/404')
    }

    return Promise.reject(result.info)
  }

  let res = {}
  let httpBody = {}
  const dataKeys = ['data', 'code', 'info', 'headers']
  const allKeys = Object.keys(result)

  dataKeys.forEach(function (key) {
    if (allKeys.indexOf(key) > -1) {
      res[key] = result[key]
    } else if (key in response) {
      res[key] = response[key]
    }
  })

  allKeys.forEach(key => {
    if (dataKeys.indexOf(key) === -1) {
      httpBody[key] = result[key]
    }
  })

  // Object.keys(httpBody).length > 0 && store.commit('updateHttpBody', httpBody)

  return res
}, (error: any) => {
  return Promise.reject(error)
})

function _get (url: string, succ: (arg0: any) => void, fail: () => void, config = {}) {
  http.get(url, config)
    .then(function (response: any) {
      typeof succ === 'function' && succ(response)
    })
    .catch(function (error: string) {
      console.error(url + ' failed, error messsage: ' + error)
      typeof fail === 'function' && fail()
    })
}

function _delete (url: string, succ: (arg0: any) => void, fail: () => void, config = {}) {
  http.delete(url, config)
    .then(function (response: any) {
      typeof succ === 'function' && succ(response)
    })
    .catch(function (error: string) {
      console.error(url + ' failed, error messsage: ' + error)
      typeof fail === 'function' && fail()
    })
}

function _post (url: string, param: any, succ: (arg0: any) => void, fail: () => void, config = {}) {
  http.post(url, param, config)
    .then(function (response: any) {
      typeof succ === 'function' && succ(response)
    })
    .catch(function (error: string) {
      console.error(url + ' failed, error messsage: ' + error)
      typeof fail === 'function' && fail()
    })
}

function _put (url: string, param: any, succ: (arg0: any) => void, fail: () => void, config = {}) {
  http.put(url, param, config)
    .then(function (response: any) {
      typeof succ === 'function' && succ(response)
    })
    .catch(function (error: string) {
      console.error(url + ' failed, error messsage: ' + error)
      typeof fail === 'function' && fail()
    })
}

export default ({ Vue }) => {
  Vue.prototype.$get = _get
  Vue.prototype.$delete = _delete
  Vue.prototype.$post = _post
  Vue.prototype.$put = _put
}
