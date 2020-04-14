<template>
  <div>
    <b-card-group>
      <b-card
              header-tag="header"
              footer-tag="footer"
              title="Audio frequency spectrum"
              footer="By Mamedov Valentin"
              header="Сервер всего с 2Gb оперативной памяти (свободен 1Gb), файлы до 1 Mb работают хорошо, дальше проблемы"      
>
        <b-card-text>
          <b-form-file
                  v-model="file"
                  :state="Boolean(file)"
                  placeholder="Choose a file or drop it here..."
                  drop-placeholder="Drop file here..."
          ></b-form-file>
        </b-card-text>
        <b-button v-on:click="uploadFile()">Upload</b-button>
      </b-card>
    </b-card-group>

    <div style="text-align: center;">
      <div v-if="loading">
        <h3>Wait a little, please!</h3>
        <div class="loader">Loading...</div>
      </div>
      <img :src="response" v-if="Boolean(response) & !loading">
    </div>
  </div>
</template>

<script>
  import api from '@/api/DragAndDrop.js'

  export default {
    data: function () {
      return {
        file: '',
        response: '',
        visible: false,
        loading: false
      }
    },
    name: 'DragAndDrop',
    methods: {
      previewFiles() {
        if (this.file == '') { 
          alert('No file');
          return 0;
        }
        var file = this.file;
        var nameArray = file.name.split('.').map((el) => {
          return el.toLowerCase();
        });
        var lastIndex = nameArray.length - 1;
        console.log(nameArray[lastIndex]);
        if (nameArray[lastIndex] !== 'mp3') {
          alert('no MP3 file');
          return 0;
        }
        if (file.size/1024/1024 > 1) {
          alert('too big for this server')
          return 0; 
        }
        return 1;
      },
      async uploadFile() {
        if (this.previewFiles() === 1) {
          this.loading = true;
          this.show();
          this.response = await api.uploadFile(this.file)
          this.loading = false;

        } else {
          this.file = '';
        }
      },
      show() {
        this.visible = true;
      },
      hide() {
        this.visible = false;
        this.file = '';
      }
    }
  }

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  body {
    background: rgba(0, 0, 0, 0.9);
  }
  img {
    width: 100%;
    height: 80%;
  }
  /* Add Animation */
  @keyframes animatetop {
    from {
      top: -300px;
      opacity: 0
    }
    to {
      top: 0;
      opacity: 1
    }
  }

/*  wait animation*/
  .loader,
  .loader:after {
    border-radius: 50%;
    width: 10em;
    height: 10em;
  }
  .loader {
    margin: 60px auto;
    font-size: 10px;
    position: relative;
    text-indent: -9999em;
    border-top: 1.1em solid rgba(255, 255, 255, 0.2);
    border-right: 1.1em solid rgba(255, 255, 255, 0.2);
    border-bottom: 1.1em solid rgba(255, 255, 255, 0.2);
    border-left: 1.1em solid #ff77d2;
    -webkit-transform: translateZ(0);
    -ms-transform: translateZ(0);
    transform: translateZ(0);
    -webkit-animation: load8 1.1s infinite linear;
    animation: load8 1.1s infinite linear;
  }
  @-webkit-keyframes load8 {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }
  @keyframes load8 {
    0% {
      -webkit-transform: rotate(0deg);
      transform: rotate(0deg);
    }
    100% {
      -webkit-transform: rotate(360deg);
      transform: rotate(360deg);
    }
  }
</style>
