import Vue from 'vue'
import Vuex from 'vuex'

import * as actions from './actions'
import * as getters from './getters'
import state from './state'
import * as mutations from './mutations'

if (!Vue.prototype.isPortal) {
	Vue.use(Vuex)
}

const block = {
  namespaced: true,
  state,
  getters,
  mutations,
  actions
}

const store = new Vuex.Store({
  modules: { [process.env.APP_SCOPE_NAME]: block },
  strict: process.env.NODE_ENV === 'development'
})

export default Vue.prototype.isPortal ? block : store
