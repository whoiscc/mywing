<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <LoginTest/>
  </div>
</template>

<script>
import LoginTest from './components/LoginTest'

export default {
  name: 'app',
  components: {
    LoginTest
  },
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  text-align: center;
}
</style>
