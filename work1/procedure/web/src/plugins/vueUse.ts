/*
* install all vue plugins here
* */

import VueI18n from 'vue-i18n'
import messages from '@/i18n'
import MgComponents from 'mg-front-end-framework'
import 'quasar-extras/animate'
import 'quasar-extras/material-icons'
import 'quasar-extras/fontawesome'
import 'quasar-extras/ionicons'
import 'quasar-extras/mdi'
import Quasar from 'quasar'


export default ({ Vue, app }: { Vue: typeof Personal.Verify, app: any}) => {
  Vue.use(VueI18n)
  if(!Vue.prototype.isPortal) {
    Vue.mixin({
      methods: {
        $mg_t (this: Personal.Verify, ...arg: any[]): string {
          return this.$t(...arg)
        }
      }
    })
  }
  // Set i18n instance on app
  app.i18n = new VueI18n({
    locale: 'zh',
    fallbackLocale: 'zh',
    messages
  })
  Vue.use(Quasar, {
    config: {}
  })
  Vue.use(MgComponents)
}
