<template>
  <div>
    <section class="section section-shaped my-0 overflow-hidden">
      <div class="shape shape-style-1 bg-gradient-default shape-skew">
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
        <span></span>
      </div>
      <div class="container py-0">
        <div class="row row-grid align-items-center">
          <div class="col-md-6 order-lg-2 ml-lg-auto">
            <div class="position-relative pl-md-5">
              <img src="img/ill/ill-2.svg" class="img-center img-fluid" />
            </div>
          </div>
          <div class="col-lg-6 order-lg-1">
            <div class="d-flex px-3">
              <div>
                <div
                  class="icon icon-shape bg-gradient-white icon-lg shadow rounded-circle text-primary"
                >
                  <i class="ni ni-single-copy-04"></i>
                </div>
              </div>
              <div class="pl-4">
                <h4 class="display-3 text-white">Envio de arquivos</h4>
                <p class="text-white">São aceitos arquivos do tipo PDF</p>
              </div>
            </div>
            <div class="card shadow-lg--hover mt-5 mb-5 shadow">
              <div class="card-body">
                <transition name="slide">
                  <div role="alert" class="alert alert-danger" v-show="alerts.error">
                    <span class="alert-inner--icon">
                      <i class="ni ni-air-baloon"></i>
                    </span>
                    <span class="alert-inner--text">
                      <span>Não foi possível salvar arquivo</span>
                    </span>
                    <!-- <button type="button" data-dismiss="alert" aria-label="Close" class="close">
                    <span aria-hidden="true">×</span>
                    </button>-->
                  </div>
                </transition>
                <transition name="slide">
                  <div role="alert" class="alert alert-primary" v-show="alerts.success">
                    <span class="alert-inner--icon">
                      <i class="ni ni-like-2"></i>
                    </span>
                    <span class="alert-inner--text">
                      <span>Arquivo enviado com sucesso</span>
                    </span>
                    <!-- <button type="button" data-dismiss="alert" aria-label="Close" class="close">
                    <span aria-hidden="true">×</span>
                    </button>-->
                  </div>
                </transition>
                <!-- FORM -->
                <div class="form-group row">
                  <label for="tag" class="col-sm-2 col-form-label" style="line-height: 0">Tag:</label>
                  <div class="col-sm-10">
                    <input
                      type="text"
                      class="form-control form-control-sm"
                      id="tag"
                      placeholder="Divida os valores por vírgula (,)"
                      v-model="tags"
                      @keyup="handleTags()"
                    />
                  </div>
                </div>
                <div class="row mb-3">
                  <div class="col-lg-12">
                    <span
                      class="badge text-uppercase badge-primary"
                      v-for="(tag, i) in form.tags"
                      :key="i"
                    >{{ tag }}</span>
                  </div>
                </div>

                <label class="form-label">Autor:</label>
                <div class="row">
                  <div class="col-sm" v-for="author in authors" :key="author.id">
                    <div class="custom-control custom-radio mb-3">
                      <input
                        type="radio"
                        name="author"
                        class="custom-control-input"
                        :id="author.id"
                        :value="author.id"
                        v-model="form.author"
                      />
                      <label class="custom-control-label" :for="author.id">{{ author.name }}</label>
                    </div>
                  </div>
                </div>

                <label class="form-label">Categoria:</label>
                <select class="custom-select custom-select-sm mb-3" v-model="form.category">
                  <option
                    v-for="category in categories"
                    :key="category.id"
                    :value="category.id"
                  >{{ category.description }}</option>
                </select>

                <div class="form-group">
                  <label for="arquivo">Arquivo:</label>
                  <input
                    type="file"
                    class="form-control-file"
                    id="arquivo"
                    ref="file"
                    @change="handleFileUpload()"
                  />
                </div>

                <button
                  type="button"
                  class="mt-4 btn btn-block btn-primary"
                  @click="upload()"
                >Enviar</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
export default {
  data() {
    return {
      tags: "",
      authors: [],
      categories: [],
      form: {
        tags: [],
        file: null,
        author: null,
        category: null
      },
      alerts: {
        error: false,
        success: false
      }
    };
  },
  created() {
    this.getAuthor();
    this.getCategory();
  },
  methods: {
    getAuthor() {
      this.$axios.get("/authors").then(response => {
        this.authors = response.data;
      });
    },
    getCategory() {
      this.$axios.get("/categories").then(response => {
        this.categories = response.data;
      });
    },
    handleTags() {
      // separa a string baseado na virgula e remove espaços e valores vazios
      this.form.tags = this.tags
        .split(",")
        .map(function(item) {
          return item.trim();
        })
        .filter(function(item) {
          return item;
        });
    },
    handleFileUpload() {
      this.form.file = this.$refs.file.files[0];
    },
    upload() {
      let form = new FormData();
      form.append("file", this.form.file);
      form.append("tags", this.form.tags);
      form.append("author", this.form.author);
      form.append("category", this.form.category);

      this.$axios
        .post("/document", form, {
          headers: {
            "Content-Type": "multipart/form-data"
          }
        })
        .then(response => {
          this.alerts.success = true;
          setTimeout(() => {
            this.alerts.success = false;
            this.form = {
              tags: [],
              file: null,
              author: null,
              category: null
            };
          }, 2000);
        })
        .catch(error => {
          this.alerts.error = true;
        });
    }
  }
};
</script>
<style>
.slide-enter-active {
  -moz-transition-duration: 0.5s;
  -webkit-transition-duration: 0.5s;
  -o-transition-duration: 0.5s;
  transition-duration: 0.5s;
  -moz-transition-timing-function: ease-in;
  -webkit-transition-timing-function: ease-in;
  -o-transition-timing-function: ease-in;
  transition-timing-function: ease-in;
}

.slide-enter-to,
.slide-leave {
  max-height: 400px;
  overflow: hidden;
}

.slide-enter,
.slide-leave-to {
  overflow: hidden;
  max-height: 0;
}
</style>
