<template lang="pug">
div
  v-stepper.mx-n4.mx-md-n4(
    v-model="stepper",
    alt-labels,
    style="box-shadow: none"
  )
    v-stepper-header
      v-stepper-step(step="1", :complete="stepper > 1")
        | Importar áudio
      v-divider
      v-stepper-step(step="2")
        | Identificando...
      v-divider
      v-stepper-step(step="3")
        | Minha música!
    v-stepper-items
      v-stepper-content(step="1")
        dropzone#dropzone(
          ref="myVueDropzone",
          style="width: 100%",
          :include-styling="false",
          :useCustomSlot="true",
          :options="dropzoneOptions",
          @vdropzone-file-added="fileAdded"
        )
          .dropzone-container
            .file-selector(v-if="!form.mp3")
              figure
                CloudUploadSvg
              | Arraste/Solte sua música ou áudio .MP3 aqui 🤘
              p.separator
                span ou
              v-btn.text-none(color="#D500F9", dark, small, depressed) Procurar...
            template(v-else)
              div(
                style="position: relative; border-radius: 15px; background-color: #f9f9f9; width: 100%; display: flex; flex-wrap: wrap"
              )
                v-row(
                  no-gutters="no-gutters",
                  style="padding: 30px; justify-content: center"
                )
                  v-col(cols="auto")
                    FakeCircularLoader(
                      :autostart="true",
                      @update="finishedLoading = $event"
                    )
                    .titleLabel.colorDark(
                      style="text-align: center; margin-top: 8px"
                    )
                      | {{ progressText }}
                      br
                    .titleLabel.colorDark(
                      style="text-align: center; margin-top: 8px; font-style: italic"
                    )
                      | {{ fileInfoText }}
                v-btn(
                  v-if="fileInfo",
                  icon,
                  style="position: absolute; top: 0; right: 0",
                  @click="removeFile"
                )
                  v-icon mdi-close
      v-stepper-content(step="2")
        v-row(
          v-if="flags.saving",
          style="height: 100%; justify-content: center; align-items: center"
        )
          v-col(cols="auto")
            v-progress-circular(
              color="rgba(200, 200, 200, 0.7)",
              size="250",
              indeterminate,
              width="6"
            )
              b(
                style="font-size: 17px; font-weight: 700; color: rgba(0, 0, 0, 0.3)"
              ) Identificando música...
        v-row(
          v-else,
          no-gutters,
          style="padding: 0; height: 100%; justify-content: center; align-items: center"
        )
          v-col(cols="auto")
            template(v-if="!importError")
              img(
                src="../assets/check-underline-circle.png",
                style="height: 256px; width: 256px; display: block; transition: 0.5s; margin: auto",
                :class="anmtImgClass"
              )
              .titleLabel.colorDark(
                style="text-align: center; transition: 0.2s",
                :class="anmtTxtClass"
              ) Concluído!
            template(v-else)
              img(
                src="../assets/close-circle.png",
                style="height: 256px; width: 256px; display: block; transition: 0.5s; margin: auto",
                :class="anmtImgClass"
              )
              .titleLabel.colorDark(
                style="text-align: center; transition: 0.2s",
                :class="anmtTxtClass"
              ) Erro!
              .titleLabel.colorDark(
                style="text-align: center; transition: 0.2s",
                :class="anmtTxtClass"
              ) {{ importError.message }}
      v-stepper-content(step="3")
        v-container 
          v-row 
            v-col(cols="6")
              .text-h4 {{ nomeDaMusica }}
              .text-subtitle-1.text--secondary {{ nomeDoArtista }}
              .text-h5 Letra
              .text-caption(style="white-space: pre-line") {{ letraDaMusica.split('\n').slice(1).join('\n') }}
            v-col(cols="6")
              img(v-if="foto != ''" :src="foto" height="300px" width="300px")
  v-row.pa-0(justify="space-between")
    v-col(cols="auto")
      v-btn(
        v-if="stepper < 2"
        text
        @click="prevBtn"
      ) {{ stepper > 1 ? 'Voltar' : 'Cancelar' }}
    v-col(cols="auto")
      v-btn(
        color="primary"
        :disabled="!finishedLoading || flags.saving || importError"
        @click="nextBtn"
      ) {{ stepper !== 3 ? 'Próximo' : 'OK' }}
</template>

<script>
import vue2Dropzone from "vue2-dropzone";
import "vue2-dropzone/dist/vue2Dropzone.min.css";
import FakeCircularLoader from "@/components/utils/FakeCircularLoader";
import axios from "axios";
const SerpApi = require("google-search-results-nodejs");
const search = new SerpApi.GoogleSearch(
  "4762345cdde17ccc19ffa060c0083f8a2d25aa46aced0407f6d2a713675541f4"
);
axios.defaults.headers.common["Access-Control-Allow-Origin"] = "*";

// Show result as JSON

const initialData = function () {
  return {
    stepper: 1,
    form: {
      mp3: null,
      file: null,
    },
    flags: {
      saving: false,
      fileAdded: false,
    },
    importError: null,
    anmtImgClass: "size-hidden",
    anmtTxtClass: "opacity-hidden",
    apiResult: "",
    letraDaMusica: "",
    wikiContent: "",
    nomeDaMusica: "",
    nomeDoArtista: "",
    search,
    foto: ""
  };
};
export default {
  components: {
    dropzone: vue2Dropzone,
    FakeCircularLoader,
  },
  props: ["visible", "bus"],
  watch: {
    visible(visible) {
      if (!visible) {
        setTimeout(() => {
          this.clear();
        }, 500);
      }
    },
    // stepper(nV) {
    //   if (nV === 2) {
    //     if (this.flags.fileAdded) {
    //       console.log(
    //         JSON.parse(JSON.stringify(this.$refs['xlsx-json'].collection))
    //       )
    //       this.itemsTable(this.$refs['xlsx-json'].collection)
    //       this.flags.fileAdded = false
    //     }
    //   } else this.$emit('change-max-width', 800)
    // },
    "flags.saving"(nV) {
      console.log("aaaaaa");
      if (!nV) {
        setTimeout(() => {
          this.anmtImgClass = "size-110";
          setTimeout(() => {
            this.anmtImgClass = "size-100";
            this.anmtTxtClass = "opacity-100";
            // console.log('tamanho 100')
          }, 500);
          // console.log('tamanho 110')
        }, 200);
      }
    },
  },
  computed: {
    progressText() {
      if (!this.fileInfo) return "";
      if (this.finishedLoading) {
        return "Finalizado!";
      } else {
        return "Carregando arquivo...";
      }
    },
    fileInfoText() {
      if (!this.fileInfo) return "";

      const i = Math.floor(Math.log(this.fileInfo.size) / Math.log(1024));
      const sizeText =
        (this.fileInfo.size / Math.pow(1024, i)).toFixed(2) * 1 +
        " " +
        ["B", "kB", "MB", "GB", "TB"][i];
      return `${this.fileInfo.name}(${sizeText})`;
    },
  },
  data() {
    return {
      dropzoneOptions: {
        autoProcessQueue: false,
        url: `fakeurl`,
        headers: {
          Authorization: `Access Token`,
        },
        paramName: function () {
          return "file[]";
        },
        includeStyling: false,
        previewsContainer: false,
        thumbnailWidth: 250,
        thumbnailHeight: 140,
        uploadMultiple: false,
        acceptedFiles: ".mp3",
        parallelUploads: 1,
      },
      fileInfo: null,
      finishedLoading: false,
      ...initialData(),
    };
  },
  async mounted() {
    // const queryResult = await this.getArtistPic("Dire Straits");
    // console.log(queryResult);
  },
  methods: {
    clear() {
      Object.assign(this.$data, initialData());
      this.user = null;
      this.$refs.myVueDropzone.removeAllFiles();
    },
    url_img(nome) {
      const url = this.getArtistPic(nome)
      return url
    },
    prevBtn() {
      switch (this.stepper) {
        case 1:
          this.$emit("close");
          break;
        case 2:
          this.stepper--;
          break;
        default:
          this.stepper--;
      }
    },
    async nextBtn() {
      switch (this.stepper) {
        case 1:
          this.stepper++;
          this.flags.saving = true;
          try {
            // api
            var formData = new FormData();
            formData.append("audio", this.form.file);

            this.apiResult = await axios.post(
              "http://127.0.0.1:5000/sendMusic",
              formData,
              {
                headers: {
                  "Content-Type": "multipart/form-data",
                },
              }
            );
            this.importError = null;
            console.log(this.apiResult);
            this.nomeDaMusica = this.apiResult.data.split("*")[0];
            this.nomeDoArtista = this.apiResult.data.split("*")[1];
            this.wikiContent = this.apiResult.data.split("*")[2];
            this.letraDaMusica = this.apiResult.data.split("*")[3];
            this.foto = await this.getArtistPic(this.nomeDoArtista);
            console.log('fotooo', this.foto)
          } catch (error) {
            this.importError = error;
            console.error(error);
          } finally {
            this.flags.saving = false;
          }
          break;
        case 2:
          this.stepper++;
          break;
        default:
          this.$emit("close");
          break;
      }
    },
    async getArtistPic(artistName) {
      console.log("oi")      
      const query = artistName.split(" ").join("+").toLowerCase().trim();
      console.log(query)
      const result = await axios.get(
        `https://cors-anywhere.herokuapp.com/https://serpapi.com/search.json?engine=google&q=${query}&google_domain=google.com&tbm=isch&ijn=0&api_key=4762345cdde17ccc19ffa060c0083f8a2d25aa46aced0407f6d2a713675541f4`,
        {
          headers: {
            "X-Requested-With": "XMLHttpRequest",
          },
        }
      )
      
      console.log(result.data.images_results[1].original);
      console.log(result)
      return result.data.images_results[1].original;
      
    },
    async fileAdded(file) {
      console.log('File Dropped => ', file)
      console.log(file.name)
      console.log(file.name.split('.')[file.name.split('.').length - 1])
      if (file.name.split('.')[file.name.split('.').length - 1]) {
        this.fileInfo = {
          name: file.name,
          size: file.size,
        };
        const reader = new FileReader();
        const readMP3Promise = new Promise((resolve) => {
          reader.onload = (evt) => resolve(evt.target.result);
        });
        reader.readAsText(file);
        this.form.mp3 = await readMP3Promise;
        this.form.file = file;
        this.flags.fileAdded = true;
      } else {
        // TODO
        alert("Tipo inválido de arquivo.");
      }
    },
    removeFile(event) {
      event.stopPropagation();
      this.finishedLoading = false;
      this.form.mp3 = null;
      this.form.file = null;
      this.fileInfo = null;
    },
  },
};
</script>

<style scoped>
.file-selector {
  padding: 55px;
  font-weight: 600;
  background-color: #f9f9f9;
  color: #4e5b69;
  z-index: 0;
  border-radius: 15px;
}
figure {
  margin: 0px;
}

.dropzone-container {
  display: flex;
  flex-direction: column;
  border-radius: 15px;
  border: 1px dashed #ccc;
  text-align: center;
  cursor: pointer;
}
#dropzone h1,
h2 {
  font-weight: normal;
}
#dropzone ul {
  list-style-type: none;
  padding: 0;
}
#dropzone li {
  display: inline-block;
  margin: 0 10px;
}
#dropzone a {
  color: #42b983;
}
.separator {
  position: relative;
  margin: 0;
}
.separator:after {
  position: absolute;
  content: "";
  height: 1px;
  width: 200px;
  background: #d8d8d8;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
#dropzone span {
  position: relative;
  background: #f9f9f9;
  padding: 0 4px;
  z-index: 9;
  font-size: 12px;
  color: #4e5b69;
}
.size-hidden {
  transform: scale(0);
}
.size-110 {
  transform: scale(1.1);
}
.size-100 {
  transform: scale(1);
}
.opacity-hidden {
  opacity: 0;
}
.opacity-100 {
  opacity: 100%;
}
</style>
