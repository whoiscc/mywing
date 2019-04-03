import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

import request from '../lib/request'
request.set({
  base: 'http://localhost:8000'
});


document.addEventListener('deviceready', () => {
  new Vue({
    render: h => h(App),
  }).$mount('#app')
}, false);
