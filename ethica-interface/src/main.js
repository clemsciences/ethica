import Vue from 'vue'
import App from './App.vue'
import axios from "axios";

import { BootstrapVue } from 'bootstrap-vue'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

axios.defaults.baseURL = "http://localhost:5010";

new Vue({
  render: h => h(App),
}).$mount('#app')
