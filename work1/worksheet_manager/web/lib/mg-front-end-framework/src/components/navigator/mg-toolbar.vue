<template>
  <q-toolbar class="bg-toolbar">
    <slot name="left">
      <q-btn flat class="absolute" @click="clickHandler">
        <img src="../../img/realtechLogo.png"/>
      </q-btn>
    </slot>
    <q-toolbar-title>
      <div class="text-center text-bold mg-title">
        {{ title }}
      </div>
    </q-toolbar-title>
    <div class="absolute right-14">
      <slot name="right" />
      <q-btn v-if="showHome">
        <q-icon name="home" @click.native="$Router.push('/')">
        </q-icon>
      </q-btn>
      <q-btn v-show="showAccount">
        <q-icon name="account_circle"/>
        <q-popover>
          <q-list link>
            <q-item>
              <q-item-main :label="userName"/>
            </q-item>
            <q-item @click.native="logout">
              <q-item-main label="退出"/>
            </q-item>
          </q-list>
        </q-popover>
      </q-btn>
    </div>
  </q-toolbar>
</template>

<script>
import { QToolbar, QBtn, QToolbarTitle, QIcon, QPopover, QList, QItem, QItemMain } from 'quasar'
export default {
  name: 'MgToolbar',
  components: {
    QToolbar, QBtn, QToolbarTitle, QIcon, QPopover, QList, QItem, QItemMain
  },
  props: {
    title: {
      type: String,
      default: ''
    },
    showAccount: {
      type: Boolean,
      default: true
    }
  },
  computed: {
    userName () {
      return this.$q.cookies.has('login_name') === true ? this.$q.cookies.get('login_name') : ''
    },
    showHome () {
      return Vue.prototype.isPortal ? true: false
    }
  },
  methods: {
    clickHandler () {
      this.$emit('left-click')
    },
    logout () {
      if (this.$q.cookies.has('login_name')) {
        this.$q.cookies.set('login_name', 'test', { expires: -1, path: '/' })
      }
      if (this.$q.cookies.has('login_uuid')) {
        this.$q.cookies.set('login_uuid', 'test', { expires: -1, path: '/' })
      }
      this.$router.go(0)
      this.$emit('logout')
    },
    goHome () {
      this.$Router.push.apply(this.$router, ['/'])
    }
  }
}
</script>

<style lang="stylus" scoped>
  .bg-toolbar
    background-color: #1D273A!important
    height 50px
    .mg-title
      font-size 30px
    .right-14
      right 14px
</style>
