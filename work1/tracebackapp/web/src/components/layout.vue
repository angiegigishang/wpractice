<template>
  <div class="full-width full-height">
    <div class="layout-wrap row items-center justify-center">
      <div v-for="item in list" class="row justify-center col-4">
        <div class="card text-center shadow-1" @click="$router.push({path: item.url}); setPageTitle(item.name)">
          <q-icon :name="item.icon" color="grey-9"/>
          <p class="caption text-grey-10 q-mt-md">{{ item.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapMutations } from 'vuex'
export default {
  data () {
    return {
      list: [
        { name: this.$mg_t('title.title2'), icon: 'dvr', url: `/report_download` },
        { name: this.$mg_t('title.title1'), icon: 'dvr', url: `/assaydaily` }
      ]
    }
  },
  created () {
    this.setPageTitle(this.$mg_t('title.main'))
  },
  methods: mapMutations(`${process.env.APP_SCOPE_NAME}`, ['setPageTitle'])
}
</script>

<style lang="stylus" scoped>
  .layout-wrap
    height calc(100vh - 100px)
    .card
      cursor pointer
      position relative
      width 200px
      padding 16px
      border-radius 6px
      .q-icon
        font-size 56px
      &:hover
        transform: scale(1.4)
</style>
