import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import svgs from './plugins/svgs'
import './plugins/styles'

Vue.config.productionTip = false

for (const svg of svgs) {
  Vue.component(svg.name, svg.component)
}

new Vue({
  vuetify,
  render: h => h(App)
}).$mount('#app')
