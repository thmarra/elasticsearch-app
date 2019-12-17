<template>
  <div style="min-height: 103vh">
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
                <div class="row">
                  <div class="col-lg-8 form-group input-group input-group-alternative">
                    <input
                      aria-describedby="addon-right addon-left"
                      placeholder="Insira seu termo de pesquisa"
                      class="form-control"
                      v-model="search"
                    />
                  </div>
                  <div class="col-lg-4">
                    <label class="mr-sm-2 sr-only" for="inlineFormCustomSelect">Preferência</label>
                    <select class="custom-select mr-sm-2" v-model="publisher">
                      <option value="" selected>Editora</option>
                      <option
                        v-for="publisher in publishers"
                        :key="publisher.id"
                        :value="publisher.id"
                      >{{ publisher.name }}</option>
                    </select>
                  </div>
                </div>
                <!-- <base-checkbox class="mb-3" v-model="exact">Ao pé da letra</base-checkbox> -->
                <div class="btn-wrapper">
                  <button
                    type="button"
                    class="btn mb-3 mb-sm-0 btn-icon btn-white"
                    @click="searchDocs()"
                  >
                    <span class="btn-inner--icon">
                      <i class="ni ni-zoom-split-in"></i>
                    </span>
                    <span class="btn-inner--text">Pesquisar</span>
                  </button>
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
              <div class="col-lg-4" v-for="d in documents" :key="d._id">
                <div class="card border-0 card-lift--hover shadow">
                  <div class="card-body py-5">
                    <h6 class="text-primary text-uppercase">
                      {{ d._source.file }}
                      <br />
                      <small class="text-muted">Publicado em {{ parseDate(d._source.published_at) }}</small>
                    </h6>
                    <p class="description mt-3">
                      Argon is a great free UI package based on Bootstrap 4
                      that includes the most important components and features.
                    </p>
                    <div>
                      <span
                        class="badge badge-primary badge-pill"
                        v-for="tag in d._source.tags"
                        :key="tag"
                      >{{ tag }}</span>
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
  </div>
</template>
<script>
import moment from "moment";
import BaseCheckbox from "../components/BaseCheckbox";

export default {
  components: {
    BaseCheckbox
  },
  data() {
    return {
      search: "",
      exact: false,
      publisher: "",
      documents: [],
      publishers: []
    };
  },
  created() {
    this.getPublisher();
  },
  methods: {
    searchDocs() {
      this.$axios.get("/document",  {params: { publisher: this.publisher, search: this.search }}).then(response => {
        this.documents = response.data.hits.hits;
      });
    },
    parseDate(value) {
      if (value) {
        return moment(value).format("DD/MM/YYYY hh:mm");
      }
      return "";
    },
    getPublisher() {
      this.$axios.get("/publishers").then(response => {
        this.publishers = response.data;
        console.log(this.publishers);
      });
    }
  }
};
</script>
<style>
</style>
