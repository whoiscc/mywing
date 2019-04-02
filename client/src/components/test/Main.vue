<template>
  <div class="test-main">
    <h1><pre>Debug Interfac</pre></h1>
    <Navigator @to="currentView = $event"></Navigator>
    <component
      :is="current"
      @login="angel = $event"
      :angel="angel"
    ></component>
  </div>
</template>

<script>
import Navigator from './Navigator'
import Login from './Login'
import Im from './Im'

export default {
  components: {
    Navigator, Login,
  },
  data() {
    return {
      currentView: 'login',
      angel: null,
    }
  },
  computed: {
    current() {
      if (this.currentView == 'login') {
        return Login;
      } else if (this.currentView == 'im') {
        return Im;
      } else {
        return null;
      }
    }
  }
}

</script>
