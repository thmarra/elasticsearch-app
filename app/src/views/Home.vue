<template>
  <div class="profile-page">
    <div class="position-relative">
      <section class="section-shaped my-0">
        <div class="shape shape-style-1 shape-default shape-skew">
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
          <span></span>
        </div>
        <div class="container shape-container d-flex">
          <div class="col px-0">
            <div class="row">
              <div class="col-lg-8">
                <h1 class="display-3 text-white">Busca avançada de arquivos</h1>
                <div class="form-group input-group input-group-alternative">
                  <input
                    aria-describedby="addon-right addon-left"
                    placeholder="Insira seu termo de pesquisa"
                    class="form-control"
                  />
                </div>
                <div class="btn-wrapper">
                  <button type="button" class="btn mb-3 mb-sm-0 btn-icon btn-white">
                    <span class="btn-inner--icon">
                      <i class="ni ni-zoom-split-in"></i>
                    </span>
                    <span class="btn-inner--text">Pesquisar</span>
                  </button>
                  <button type="button" class="btn btn-1 btn-neutral">Upload</button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>

    <section class="section section-lg pt-lg-0 mt--200">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-12">
            <div class="row row-grid">
              <div class="col-lg-4">
                <div class="card border-0 card-lift--hover shadow">
                  <div class="card-body py-5">
                    <h6 class="text-primary text-uppercase">
                      Nome do arquivo.pdf
                      <br />
                      <small class="text-muted">caminho/do/arquivo</small>
                    </h6>
                    <p class="description mt-3">
                      Argon is a great free UI package based on Bootstrap 4
                      that includes the most important components and features.
                    </p>
                    <div>
                      <span class="badge badge-primary badge-pill">design</span>
                      <span class="badge badge-primary badge-pill">system</span>
                      <span class="badge badge-primary badge-pill">creative</span>
                    </div>
                    <button type="button" class="btn btn-sm mt-4 btn-primary">Download</button>
                    <button
                      type="button"
                      class="btn btn-sm mt-4 btn-outline-primary"
                      @click="showModal = true"
                    >Alterar categoria</button>
                    <label class="form-label mt-3">Nova categoria:</label>
                <select class="custom-select custom-select-sm mb-3">
                  <option selected>Open this select menu</option>
                  <option value="1">One</option>
                  <option value="2">Two</option>
                  <option value="3">Three</option>
                </select>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <modal :show.sync="showModal">
      <template slot="header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
      </template>
      <div>...</div>
      <template slot="footer">
        <base-button type="secondary" @click="showModal = false">Close</base-button>
        <base-button type="primary">Save changes</base-button>
      </template>
    </modal>

  </div>
</template>
<script>
import Modal from '../components/Modal'

export default {
    name: "home",
    componenets: {
        Modal
    },
    data() {
        return {
            showModal: false
        }
    }
};
</script>
<style>
</style>
