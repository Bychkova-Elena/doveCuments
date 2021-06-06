<template>
  <div>
    <section class="section">
      <div class="container is-fluid">
          <h1 class="title has-text-info">
            Курьерам
          </h1>
          <h2 class="subtitle has-text-info">
            Станьте нашим курьером!
          </h2>
      <div class="columns">
        <div class="column content">
          <p>Вы нам подходите, если:</p>
          <ul>
            <li>Вам 18 и более лет;</li>
            <li>Вы владеете Русским языком;</li>
            <li>Вы опрятно выглядите;</li>
            <li>Вы хотите иметь постоянный или дополнительный заработок, передвигаясь по городу и общаясь с интересными людьми</li>
          </ul>
        </div>
        <div class="column">
           <figure class="image">
            <img src="../assets/courier.png" alt="курьер" />
          </figure>
        </div>
      </div>
      <div class="columns">
      <div class="column is-6 is-offset-3">
          <h2 class="subtitle has-text-info">
            Заполните небольшую форму, и мы Вам перезвоним!
          </h2>
           <form @submit.prevent="submitForm">
          <div class="field">
             <label>ФИО: <span class="has-text-danger">*</span></label>
            <div class="control">
               <input
                class="input"
                type="text"
                placeholder="ФИО"
                v-model="fio"
              />
            </div>
          </div>

          <div class="field">
             <label>Телефон: <span class="has-text-danger">*</span></label>
            <div class="control">
               <input
                class="input"
                type="tel"
                placeholder="Телефон"
                v-model="phone"
              />
            </div>
          </div>

          <div class="notification is-danger" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
          </div>

          <div class="field">
            <p class="mb-3">
              <span class="has-text-danger">*</span> - Поля, обязательные для заполнения
            </p>
            <div class="control">
              <button class="button is-link">Хочу стать курьером</button>
            </div>
          </div>
        </form>
        </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

export default {
    data() {
    return {
      fio: '',
      phone: '',
      errors: [],
    }
    },
 
  mounted() {
    document.title = 'Курьерам | DoveCuments'
  },

   methods: {
    async submitForm() {
      this.errors = [];
      if (this.fio === "") {
        this.errors.push("Не указано фио!");
      }
      if (this.phone === "") {
        this.errors.push("Не указан телефон!");
      }
      if (!this.errors.length) {
        const data = {
          fio: this.fio,
          phone: this.phone
        };

        await axios
          .post("/api/v1/create-app/", data)
          .then((response) => {
            this.$router.push("/");
            toast({
              message: "Заявка отправлена!",
              type: "is-success",
              dismissible: true,
              pauseOnHover: true,
              duration: 2000,
              position: "bottom-right",
            });
          })
          .catch((error) => {
            this.errors.push("Что-то пошло не так. Попробуйте ещё раз.");
            console.log(error.response)

          });
      }
    },
  },

}
</script>

<style lang="scss" scoped>
.image {
  width:50%;
  margin-left:30%;
  margin-top:-10%;
}
</style>
