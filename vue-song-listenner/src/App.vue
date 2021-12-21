<template lang="pug">
  v-app
    v-app-bar(
      app
      color="grey darken-4"
      dark
      flat
      height="100"
    )
      .d-flex.align-center
        v-img(
          class="shrink mr-2"
          contain
          src="./assets/logo.png"
          transition="scale-transition"
          width="100"
        )

      v-spacer

      v-btn(rounded elevation="0" color="secondary" dark @click="dialog.aboutUs = true")
        .mr-2 Quem somos
        v-icon mdi-account-group

    v-main
      v-container
        v-row#song-finder.mb-16
          v-col(cols=12)
            .mt-12.text-h5.font-weight-bold.text-center.text-uppercase(style="color: #FFC107")
              v-icon(color="#FFC107") mdi-music
              | &nbsp;Bem-vindo ao musiCIn&nbsp;
              v-icon(color="#FFC107") mdi-music
          v-col(cols=12)
            .text-h2.font-weight-medium.text-center Encontre sua música
          v-col(cols=12 style="position: relative;")
            button.mt-6.listen-button(@click="openDialog") Achar
        v-row#song-listen.mt-16
          v-col(cols=12)
            .text-h3.font-weight-medium
              v-icon(x-large dark) mdi-tray-arrow-down
              | &nbsp;Músicas para baixar
          v-col(cols=12)
            v-slide-group(show-arrows dark)
              v-slide-item(v-for='song in songs' :key='songs' v-slot='{ active, toggle }')
                a.text-decoration-none(:href="song.file" download)
                  v-card.ma-4(color="grey lighten-1" height='200' width='200' @click)
                    v-img.align-end(
                      :src="song.image"
                      gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                      )
                      .pa-3.text-h6.font-weight-medium.break-word {{ song.name }}
      v-dialog(v-model="dialog.aboutUs" max-width="800")
        v-card.px-2.px-md-3.py-3.py-md-4
          v-toolbar.toolbar-settings.text-settings
            h6.text-h6.font-weight-medium.break-word Membros
            v-spacer
          v-btn(
            icon
            absolute
            top
            right
            style="z-index: 5"
            @click="dialog.aboutUs = false"
          )
            v-icon mdi-close
          VuePerfectScrollbar
            v-card-text.text-md-left
              v-row
                v-col(cols="auto" v-for="member in members")
                  a.text-decoration-none(:href="member.url" target="_blank")
                    v-card.ma-4(color="grey lighten-1" height='200' width='200' @click)
                      v-img.align-end(
                        :src="member.image"
                        gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                        )
                        .pa-3.white--text.text-h6.font-weight-medium.break-word {{ member.name }}
      v-dialog(v-model="dialog.find" max-width="1000")
        v-card.px-2.px-md-3.py-3.py-md-4
          v-toolbar.toolbar-settings.text-settings
            h6.text-h6.font-weight-medium.break-word Achar música
            v-spacer
          v-btn(
            icon
            absolute
            top
            right
            style="z-index: 5"
            @click="dialog.find = false"
          )
            v-icon mdi-close
          VuePerfectScrollbar
            v-card-text.text-md-left
              SongFinder(:visible="dialog.find")
    v-footer(dark padless)
      v-card.indigo.darken-4.white--text.text-center(flat tile style="width: 100%")
        v-card-text
          v-row(justify="center")
            v-col(cols="auto")
              v-img.text-center(
                class="shrink mr-2"
                contain
                src="./assets/logo.png"
                transition="scale-transition"
                width="100"
              )
        v-card-text.white--text.pt-0
          | Dúvidas ou comentários?
        v-divider
        v-card-text.white--text
          | {{ new Date().getFullYear() }} &mdash; 
          strong CIn - UFPE
</template>

<script>
import VuePerfectScrollbar from 'vue-perfect-scrollbar'
import SongFinder from './components/SongFinder'

export default {
  name: 'App',
  components: {
    VuePerfectScrollbar,
    SongFinder
  },
  data() {
    return {
      dialog: {
        find: false,
        aboutUs: false
      },
      songs: [
        {
          name: 'Love of My Life',
          image: require('../public/files/mp3/images/love-of-my-life.jpg'),
          file: require('../public/files/mp3/Queen - Love Of My Life.mp3')
        },
        {
          name: 'Put Your Head On My Shoulder',
          image: require('../public/files/mp3/images/put-your-head-on-my-shoulder.jpg'),
          file: require('../public/files/mp3/Paul Anka - Put Your Head On My Shoulder.mp3')
        },
        {
          name: 'Somebody To Love',
          image: require('../public/files/mp3/images/somebody-to-love.jpg'),
          file: require('../public/files/mp3/Queen - Somebody To Love.mp3')
        },
        {
          name: 'Stand by Me',
          image: require('../public/files/mp3/images/stand-by-me.jpg'),
          file: require('../public/files/mp3/Ben E.King - Stand by Me.mp3')
        },
        {
          name: 'Take On Me',
          image: require('../public/files/mp3/images/take-on-me.jpg'),
          file: require('../public/files/mp3/a-ha - Take On Me.mp3')
        },
        {
          name: 'Love of My Life',
          image: require('../public/files/mp3/images/love-of-my-life.jpg'),
          file: require('../public/files/mp3/Queen - Love Of My Life.mp3')
        },
        {
          name: 'Put Your Head On My Shoulder',
          image: require('../public/files/mp3/images/put-your-head-on-my-shoulder.jpg'),
          file: require('../public/files/mp3/Paul Anka - Put Your Head On My Shoulder.mp3')
        },
        {
          name: 'Somebody To Love',
          image: require('../public/files/mp3/images/somebody-to-love.jpg'),
          file: require('../public/files/mp3/Queen - Somebody To Love.mp3')
        },
        {
          name: 'Stand by Me',
          image: require('../public/files/mp3/images/stand-by-me.jpg'),
          file: require('../public/files/mp3/Ben E.King - Stand by Me.mp3')
        },
        {
          name: 'Take On Me',
          image: require('../public/files/mp3/images/take-on-me.jpg'),
          file: require('../public/files/mp3/a-ha - Take On Me.mp3')
        },
      ],
      members: [
        {
          name: 'Guilherme Lopes',
          image: 'https://avatars.githubusercontent.com/u/33431002?v=4',
          url: 'https://github.com/gui555pl'
        },
        {
          name: 'Igor Henrique',
          image: 'https://avatars.githubusercontent.com/u/33430966?v=4',
          url: 'https://github.com/ihsrp1'
        },
        {
          name: 'Vinícius Guedes',
          image: 'https://avatars.githubusercontent.com/u/33430962?v=4',
          url: 'https://github.com/vguedesv'
        },
        {
          name: 'João Pedro',
          image: require('./assets/pedro.jpg'),
          url: 'https://github.com/jpedro-sdr'
        },
        {
          name: 'Humberto',
          image: 'https://cdn.discordapp.com/avatars/383331330588409859/0968a69a3ecaa60ef074daf7f48da7bb.webp?size=160',
          url: 'https://github.com/ihsrp1/ProjSinais'
        },
      ]
    }
  },
  methods: {
    openDialog() {
      this.dialog.find = true
    }
  }
};
</script>

<style scoped>
.v-main {
  background: #4A148C;
  color: rgba(255, 255, 255, 0.952)
}

.listen-button {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 200px;
  height: 50px;
  text-align: center;
  line-height: 50px;
  font-size: 20px;
  color: #fff;
  text-decoration: none;
  font-family: sans-serif;
  box-sizing: border-box;
  background: linear-gradient(90deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
  background-size: 400%;
  border-radius: 30px;
  z-index: 5;
  opacity: 1;
  transition: 0.5s;
}

.listen-button:hover {
  animation: animate 8s linear infinite;
}

@keyframes animate{
    0%{
      background-position: 0%;
    }
    100%{
      background-position: 400%;
    }
}

.listen-button:before{
  border-radius: 10px;
  content: '';
  position: absolute;
  top: -5px;
  left: -5px;
  right: -5px;
  bottom: -5px;
  z-index: -1;
  background: linear-gradient(90deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
  background-size: 400%;
  opacity: 0;
  transition: 0.5s;
}

.listen-button:hover:before{
  filter: blur(20px);
  opacity: 1;
  background: linear-gradient(90deg, #03a9f4, #f441a5, #ffeb3b, #03a9f4);
}

/* DIALOG */

.toolbar-settings {
  max-height: 64px;
  box-shadow: none !important;
  border-radius: 100px 100px 0px 0px;
}

.text-settings {
  font-family: 'Poppins', Roboto;
  font-style: normal;
  font-weight: 500;
  font-size: 18px;
  line-height: 20px;
  letter-spacing: 0.4px;
}
</style>
