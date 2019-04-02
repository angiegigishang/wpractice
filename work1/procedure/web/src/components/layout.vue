<template>
  <div class="full-width full-height">
    <div class="layout-wrap row items-center justify-center">
      <div v-for="item in list" :key="item.url" class="row justify-center col-4">
        <div class="card text-center shadow-1" @click="$router.push({path: item.url}); setPageTitle(item.name)">
          <q-icon :name="item.icon" color="grey-9"/>
          <p class="caption text-grey-10 q-mt-md">{{ item.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">

import { Vue, Component, Watch } from "vue-property-decorator";
import { mapMutations, mapState } from 'vuex';

interface list {
    name: string;
    icon: string;
    url: string;
}

@Component({
  created () {
    this['setPageTitle'](this['$mg_t']('title.main'))
  },
  computed: {
    ...mapState(<string>process.env.APP_SCOPE_NAME, ['titles'])
  },
  methods: {
    ...mapMutations(<string>process.env.APP_SCOPE_NAME, ['setPageTitle'])
  }
})
export default class Layout extends Vue {
  $mg_t: any
  list: list[] = []

  @Watch('titles', { immediate: true, deep: true })
  listRender (val) {
    let arr: list[] = []
    for (let i = 0;i < val.length;i++) {
      arr[i] = { name : val[i].name + ' ' + val[i].description, icon: 'dvr', url: `/choose/${val[i].code}`}
    }
    this['list'] = arr
  }
  
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
