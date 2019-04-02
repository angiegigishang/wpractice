/// <reference path="./main.d.ts" />
import Vue from 'vue'
import router from './router'
import store from './store'
import './styles/quasar.styl'
import './statics/global.css'
import './statics/iconfont.css'
import './statics/iconfont.js'

const isPortal = Vue.prototype.isPortal

Vue.config.productionTip = false

const name = process.env.APP_SCOPE_NAME
const Router: object | any[] = isPortal ? window[window['poolName']]['router'] : router
const Store: object | any[] = isPortal ? window[window['poolName']]['store'] : store

let plugins:any[] = []


if (!Vue.prototype.isPortal) {
    let subPlugins: any[] = [
        import('./plugins/vueMixin'),
        import('./plugins/vueUse'),
        import('./plugins/httpJs')
    ]
    Promise.all([
        ...subPlugins,
        import('./App.vue')
    ]).then(res => {
        const App = res[res.length - 1].default
        res = res.slice(0, res.length - 1)
        const app = {
          el: `#vue`,
          router: <any>Router,
          store: <any>Store,
          render: (h) => h(App)
        }
        plugins = [...plugins, ...res]
        plugins.forEach(plugin => plugin.default({ app, router: Router, store: Store, Vue }))
        new Vue(app)
    })
} else {
    Promise.all([
        import('micro-frontends-server'),
        import('@/i18n')
    ]).then(res => {
        const CreateRegister = res[0].CreateRegister
        const lang = res[1].default
        const register = new CreateRegister({
          name: (<string>name),
          poolName: window['poolName']
        })
        const that = register.registerModule(store).addRoutes(router as any)['addLang'](lang.zh, lang.en)
        plugins.forEach(plugin => plugin.default({router: that.pool.router, store: that.pool.store, Vue }))
    })
}

/* eslint-disable no-new */


