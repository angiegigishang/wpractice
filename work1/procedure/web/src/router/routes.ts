import Vue from 'vue'
const IS_PORTAL = !!Vue.prototype.isPortal
const APP_NAME = process.env.APP_SCOPE_NAME

function load (component: any) {
  return () => import(`@/components/${component}.vue`)
}
const routes: any = [
  {
    path: !IS_PORTAL ? '/' : `/items/${APP_NAME}`,
    component: load('index'),
    children: [
      { path: '', component: load('layout') },
      { path: '/choose/:id', component: load('choose'), props: true},
      { path: '/history', component: load('history'), children: [
        {
          path: 'detail/:id/:pro/:op',
          component: load('historyDetail'),
          props: true
        },
        {
          path: 'run/:id/:pro',
          component: load('historyRunning'),
          props:true
        }
      ]},
      { path: '*', component: load('Error404')}
    ]
  }// ,
  // { path: !IS_PORTAL ? '*' : `/items/${APP_NAME}/*`, component: load('Error404'), name: `${APP_NAME}-404` }
]

export default routes

