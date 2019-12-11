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
                <div role="alert" class="alert alert-danger alert-dismissible">
                  <span class="alert-inner--icon">
                    <i class="ni ni-like-2"></i>
                  </span>
                  <span class="alert-inner--text">
                    <span>
                      <strong>primary!</strong> This is a primary alert—check it out!
                    </span>
                  </span>
                  <button type="button" data-dismiss="alert" aria-label="Close" class="close">
                    <span aria-hidden="true">×</span>
                  </button>
                </div>
                <!-- FORM -->
                <div class="form-group row">
                  <label for="tag" class="col-sm-2 col-form-label" style="line-height: 0">Tag:</label>
                  <div class="col-sm-10">
                    <input
                      type="email"
                      class="form-control form-control-sm"
                      id="tag"
                      placeholder="Email"
                    />
                    <small>Divida os valores por vírgula (,)</small>
                  </div>
                </div>
                <div class="row mb-3">
                  <div class="col-lg-12">
                    <span class="badge text-uppercase badge-primary">primary</span>
                    <span class="badge text-uppercase badge-primary">primary</span>
                    <span class="badge text-uppercase badge-primary">primary</span>
                    <span class="badge text-uppercase badge-primary">primary</span>
                    <span class="badge text-uppercase badge-primary">primary</span>
                    <span class="badge text-uppercase badge-primary">primary</span>
                    <span class="badge text-uppercase badge-primary">primary</span>
                    <span class="badge text-uppercase badge-primary">primary</span>
                  </div>
                </div>

                <label class="form-label">Dono:</label>
                <div class="row">
                  <div class="col-sm">
                    <div class="custom-control custom-radio mb-3">
                      <input
                        name="custom-radio-1"
                        class="custom-control-input"
                        id="customRadio1"
                        type="radio"
                      />
                      <label class="custom-control-label" for="customRadio1">Aaaaaa</label>
                    </div>
                  </div>
                  <div class="col-sm">
                    <div class="custom-control custom-radio mb-3">
                      <input
                        name="custom-radio-1"
                        class="custom-control-input"
                        id="customRadio1"
                        type="radio"
                      />
                      <label class="custom-control-label" for="customRadio1">Bbbbb</label>
                    </div>
                  </div>
                  <div class="col-sm">
                    <div class="custom-control custom-radio mb-3">
                      <input
                        name="custom-radio-1"
                        class="custom-control-input"
                        id="customRadio1"
                        type="radio"
                      />
                      <label class="custom-control-label" for="customRadio1">Ccccc</label>
                    </div>
                  </div>
                </div>

                <label class="form-label">Categoria:</label>
                <select class="custom-select custom-select-sm mb-3">
                  <option selected>Open this select menu</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>

                <vue-dropzone ref="myVueDropzone" id="dropzone" :options="dropzoneOptions"></vue-dropzone>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>
<script>
import vue2Dropzone from "vue2-dropzone";
import "vue2-dropzone/dist/vue2Dropzone.min.css";

export default {
  components: {
    vueDropzone: vue2Dropzone
  },
  data() {
    return {
      dropzoneOptions: {
        url: "https://httpbin.org/post",
        thumbnailWidth: 150,
        maxFilesize: 0.5,
        headers: { "My-Awesome-Header": "header value" }
      },
      file: null,
      file2: null
    };
  }
};
</script>
<style>
</style>
