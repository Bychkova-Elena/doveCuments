<template>
  <div>
    <section class="section">
      <div class="container is-fluid">
        <div class="">
          <h1 class="title has-text-info">
            Сервис курьерской доставки документов
          </h1>
          <div class="columns">
            <div class="column">
          <h2
            class="title has-text-info is-2"
            v-for="contact in contacts"
            :key="contact.id"
          >
            <strong>{{ contact.phone }}</strong>
          </h2>
          <figure class="image">
            <img src="../assets/dove.png" alt="голубь" />
          </figure>
          </div>
          <div class="column">
            <h3 class="mb-1">Узнайте примерную стоимость доставки</h3>
            <TariffsTable></TariffsTable>
          </div>
          </div>
        </div>

        <div class="mt-6">
          <h1 class="title has-text-info has-text-centered">Виды доставок</h1>
          <div
            class="is-flex is-justify-content-space-evenly is-align-content-center is-flex-wrap-wrap"
          >
            <div
              class="card m-3"
              v-for="delivery in deliveries"
              :key="delivery.id"
            >
              <header class="card-header">
                <p class="card-header-title">
                  {{ delivery.name }}
                </p>
              </header>
              <div class="card-content">
                <div class="content">
                  {{ delivery.description }}
                </div>
              </div>
            </div>
          </div>
          <div
            class="is-flex is-justify-content-center is-align-self-center mt-6"
          >
            <router-link
              to="/order-form"
              class="button is-rounded is-warning is-outlined"
              >Заказать доставку</router-link
            >
          </div>
        </div>
      </div>
    </section>

    <div class="mt-3 p-6 has-background-light">
      <h1 class="title has-text-info has-text-centered">
        Необходимо оформлять заявки регулярно? <br />
        Зарегистрируйтесь! Или заполните короткую форму для разовой доставки на
        сайте.
      </h1>
      <div class="field is-grouped mt-6 is-flex is-justify-content-center">
        <button class="button is-rounded is-warning mr-3">
          Зарегистрироваться
        </button>
        <router-link
          to="/order-form"
          class="button ml-6 is-rounded is-warning is-outlined"
          >Заказать доставку</router-link
        >
      </div>
    </div>

    <section class="section">
      <div class="container is-fluid">
        <div class="mt-3">
          <h1 class="title has-text-info has-text-centered">Способы оплаты</h1>
          <div
            class="is-flex is-justify-content-space-evenly is-align-content-center is-flex-wrap-wrap mt-6"
          >
            <div class="card m-3" v-for="payment in payments" :key="payment.id">
              <header class="card-header">
                <p class="card-header-title">
                  {{ payment.name }}
                </p>
              </header>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import TariffsTable from "@/components/TariffsTable.vue";

export default {
  data() {
    return {
      payments: [],
      deliveries: [],
      contacts: []
    };
  },
    components: {
    TariffsTable
  },
  mounted() {
    document.title = 'Доставка документов | DoveCuments'
    this.getPayments(), this.getDeliveries(), this.getContacts();
  },
  methods: {
    getPayments() {
      axios
        .get("api/v1/payment/")
        .then(response => {
          this.payments = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    getDeliveries() {
      axios
        .get("api/v1/delivery/")
        .then(response => {
          this.deliveries = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    },

    getContacts() {
      axios
        .get("api/v1/contacts/")
        .then(response => {
          this.contacts = response.data;
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss" scoped>
.image{
 width:30%;
 margin-left:40%;
}

</style>
