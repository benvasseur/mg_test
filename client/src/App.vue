<template>
  <div class="h-100">
    <top-Bar></top-Bar>

    <transition name="fade" mode="out-in">
      <router-view></router-view>
    </transition>
  </div>
</template>

<script>
import topBar from './components/topBar.vue';

export default {
  name: 'app',

  components: {
    topBar
  },

  data () {
    return {}
  }
}
</script>

<style lang="scss">
body{
  height: 100vh;
}
</style>
