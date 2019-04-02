<template>
  <div class="mg-notFound">
    <div class="fixed-center text-center">
      <p>
        <img
          src="~@/assets/sad.svg"
          style="width:30vw;max-width:150px;"
        >
      </p>
      <p class="text-faded">Sorry, nothing here...<strong>(404)</strong></p>
      <q-btn
        color="secondary"
        style="width:200px;"
        @click="$router.replace('/')"
      >Go back</q-btn>
    </div>
  </div>
</template>

<!-- <script>
  export default {
    mounted () {
      // sub item register, not remove!
      if (this.isPortal) {
        this.$store.commit('finish')
      }
    }
  }
</script> -->

<style lang="stylus" scoped>
  .mg-notFound
    position fixed
    top 0
    left 0
    right 0
    bottom 0
    background white
    z-index 8888
    >div
      z-index 8889
</style>
