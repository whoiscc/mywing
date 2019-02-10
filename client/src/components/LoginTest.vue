<template>
  <div class="login-test">
    <button type="button" @click="onLogin">Login</button>
    <button type="button" @click="onLogout">Logout</button>
    <button type="button" @click="onRequest">Test Request</button>
    <div>{{ angel || 'Make a request to see something.' }}</div>
    <div v-if="error" style="color: red">{{ error }}</div>
  </div>
</template>

<script>
import request from '../../lib/request'

export default {
  data() {
    return {
      angel: null,
      error: null,
    }
  },
  methods: {
    onLogin() {
      request.login('debug-ticket-create-angel').then(() => {
        console.log('login finished')
      })
    },
    onLogout() {
      request.logout().then(() => {
        this.angel = null
        console.log('logout finished')
      })
    },
    onRequest() {
      request.get('/angel').then(angel => {
        this.angel = angel
        this.error = null
      }).catch(err => {
        this.error = err
      })
    },
  }
}
</script>
