import Vue from 'vue'
import App from './App.vue'
import axios from "axios";
import "./services/bootstrap"
import {router} from "@/services/router";

Vue.config.productionTip = false

axios.defaults.baseURL = process.env.VUE_APP_SITE_API_URL;

new Vue({
  render: h => h(App),
  router,

}).$mount('#app')
