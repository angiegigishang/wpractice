<template>
  <q-layout view="HHH lpr fff">
    <q-layout-header v-if="$route.path !== `${isPortal ? `/items/${process.env.APP_SCOPE_NAME}/showpage`: '/showpage'}`">
      <mg-toolbar :title="displayTitle" @left-click="$router.push('/')"></mg-toolbar>
    </q-layout-header>

    <q-page-container>
      <router-view></router-view>
    </q-page-container>
  </q-layout>
</template>

<script>
import { mapState, mapMutations } from 'vuex'
export default {
  created () {
    typeof window !== 'undefined' && (window.onbeforeunload = e => {
      sessionStorage.setItem('state', JSON.stringify(this.$store.state))
    })
    console.log(this.$router)
  },
  computed: {
    ...mapState(`${process.env.APP_SCOPE_NAME}`, ['pageTitle']),
    displayTitle () {
      return this.pageTitle || this.$mg_t('title.main')
    }
  },
  mounted () {
    // sub item register, not remove!
    if (this.isPortal) {
      this.$store.commit('finish')
    }
  },
  methods: {
    ...mapMutations(['updateUserInfo'])
  }
}
</script>

<style lang="stylus" scoped>
  @import '~variables'
  .content
    margin-top 100px
    font-size 24px
    color $tertiary
</style>
