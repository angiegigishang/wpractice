import Vue from 'vue'
const IS_PORTAL = !!Vue.prototype.isPortal
const APP_NAME = process.env.APP_SCOPE_NAME

function load (component) {
  return () => import(`@/components/${component}.vue`)
}

export default
[
  {
    path: !IS_PORTAL ? '/' : `/items/${APP_NAME}`,
    component: load('index'),
    children: [
      { path: '', component: load('layout') },
      { path: '*', component: load('Error404')}
    ]
  }// ,
  // { path: !IS_PORTAL ? '*' : `/items/${APP_NAME}/*`, component: load('Error404'), name: `${APP_NAME}-404` }
]
