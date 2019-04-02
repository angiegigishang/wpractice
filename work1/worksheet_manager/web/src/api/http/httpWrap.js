import Vue from 'vue'

const $get = Vue.prototype.$get
export function _get (url, succ, fail, config = {}) {
  if (process.env.COMPILE_MODE === 'lib') {
    config['（scopeName'] = process.env.APP_SCOPE_NAME
  }
  $get(url, succ, fail, config)
}

const $delete = Vue.prototype.$delete
export function _delete (url, succ, fail, config = {}) {
  if (process.env.COMPILE_MODE === 'lib') {
    config['scopeName'] = process.env.APP_SCOPE_NAME
  }
  $delete(url, succ, fail, config)
}

const $post = Vue.prototype.$post
export function _post (url, param, succ, fail, config = {}) {
  if (process.env.COMPILE_MODE === 'lib') {
    config['scopeName'] = process.env.APP_SCOPE_NAME
  }
  $post(url, param, succ, fail, config)
}

const $put = Vue.prototype.$put
export function _put (url, param, succ, fail, config = {}) {
  if (process.env.COMPILE_MODE === 'lib') {
    config['scopeName'] = process.env.APP_SCOPE_NAME
  }
  $put(url, param, succ, fail, config)
}
