<template>
  <q-layout view="HHH lpr fff">
    <q-layout-header>
      <mg-toolbar :title="displayTitle" @left-click="$router.push('/')"></mg-toolbar>
    </q-layout-header>

    <q-page-container>
      <router-view></router-view>
    </q-page-container>
  </q-layout>
</template>

<script lang="ts">
import { mapState, mapMutations } from 'vuex';
import { Vue, Component } from "vue-property-decorator";
import http from 'http/serverRequests'

@Component({
  created () {
    typeof window !== 'undefined' && (window.onbeforeunload = e => {
      sessionStorage.setItem('state', JSON.stringify(this['$store'].state))
    })
    this['getAllPro']()
  },
  computed: {
    ...mapState(<string>process.env.APP_SCOPE_NAME, ['pageTitle']),
    displayTitle (): string {
      return this['pageTitle']
    }
  },
  mounted () {
    // sub item register, not remove!
    if (this['isPortal']) {
      this['$store'].commit('finish')
    }
  },
  methods: {
    ...mapMutations(<string>process.env.APP_SCOPE_NAME, ['setPageTitle', 'putTitles'])
  }
})
export default class Index extends Vue {
  getAllPro (): Promise<any>{
    return new Promise<any>((resolve:()=>void,reject:()=>void) => {
      http['getAllPro'](res => {
        if (this['responseValidate'](res)) {
          this['putTitles'](res.data)
          resolve()
        }
      }, err => {

      })
    })
  }
};
</script>

<style lang="stylus" scoped>
  @import '~variables'
  .content
    margin-top 100px
    font-size 24px
    color $tertiary
</style>
