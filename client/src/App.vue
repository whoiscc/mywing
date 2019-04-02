<template>
  <div id="app">
    <DebugMain/>
  </div>
</template>

<script>
import DebugMain from './components/test/Main'

export default {
  name: 'app',
  components: {
    DebugMain
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  /* text-align: center; */
}
</style>
