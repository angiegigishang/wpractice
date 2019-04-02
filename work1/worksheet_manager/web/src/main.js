import Vue from 'vue'
import router from './router'
import store from './store'
import './styles/quasar.styl'

const isPortal = Vue.prototype.isPortal

Vue.config.productionTip = false

const name = process.env.APP_SCOPE_NAME
const Router = isPortal ? window[window.poolName]['router'] : router
const Store = isPortal ? window[window.poolName]['store'] : store

let plugins = []


if (!Vue.prototype.isPortal) {
	let subPlugins = [
		import('./plugins/vueMixin'),
		import('./plugins/vueUse'),
		import('./plugins/httpJs'),
		import('./plugins/echarts')
	]
	Promise.all([
		...subPlugins,
		import('./App.vue')
	]).then(res => {
		const App = res[res.length - 1].default
		res = res.slice(0, res.length - 1)
		const app = {
		  el: `#vue`,
		  router: Router,
		  store: Store,
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
		  name,
		  poolName: window.poolName
		})
		const that = register.registerModule(store).addRoutes(router).addLang(lang.zh, lang.en)
		plugins.forEach(plugin => plugin.default({router: that.pool.router, store: that.pool.store, Vue }))
	})
}

/* eslint-disable no-new */


