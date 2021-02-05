import Vue from 'vue'
import App from './App.vue'
import axios from "axios";

import { BootstrapVue } from 'bootstrap-vue'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)

Vue.config.productionTip = false

axios.defaults.baseURL = process.env.VUE_APP_SITE_API_URL;

new Vue({
  render: h => h(App),
}).$mount('#app')
