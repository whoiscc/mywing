<template>
  <div class="login-test">
    <button type="button" @click="onLogin">Login</button>
    <button type="button" @click="onLogout">Logout</button>
    <button type="button" @click="onRequest">Test Request</button>
    <div>{{ message || 'Push a button to see something.' }}</div>
    <div v-if="error" style="color: red">{{ error }}</div>
  </div>
</template>

<script>
import request from '../../lib/request'

export default {
  data() {
    return {
      message: null,
      error: null,
    }
  },
  methods: {
    onLogin() {
      request.login('debug-ticket-create-angel', true).then(() => {
        this.message = 'Login finished'
        this.error = null
      }).catch(err => {
        this.error = err
      })
    },
    onLogout() {
      request.logout().then(() => {
        this.message = 'Logout finished'
        this.error = null
      }).catch(err => {
        this.error = err
      })
    },
    onRequest() {
      request.get('/angel').then(angel => {
        this.message = angel
        this.error = null
      }).catch(err => {
        this.error = err
      })
    },
  }
}
</script>
