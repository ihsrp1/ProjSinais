import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';
import pt from 'vuetify/es5/locale/pt'

Vue.use(Vuetify);

export default new Vuetify({
  lang: {
    locales: { pt },
    current: 'pt'
  },
  icons: {
    iconfont: 'mdi'
  },
  theme: {
    options: { customProperties: true },
    themes: {
      light: {
        primary: '#4A148C',
        secondary: '#D500F9',
        accent: '#00bcd4',
        error: '#ff5722',
        warning: '#FF9800', // '#ffc107',
        info: '#607d8b',
        success: '#00bcd4'
      },
      dark: {
        primary: '#6A1B9A',
        secondary: '#03a9f4',
        accent: '#00bcd4',
        error: '#ff5722',
        warning: '#FF9800', // '#ffc107',
        info: '#607d8b',
        success: '#00bcd4'
      }
    }
  }
});
