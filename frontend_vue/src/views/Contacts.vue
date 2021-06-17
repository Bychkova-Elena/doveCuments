<template>
  <section class="section">
      <div class="columns">
      <div class="column is-6 is-offset-3">
          <h1 class="title has-text-info">
            Контакты
          </h1>
      <div class="content has-background-warning p-6" v-for = "contact in contacts" :key="contact.id">
    <p><strong>Телефон: </strong>{{contact.phone}}</p>
    <p><strong>Email: </strong>{{contact.email}}</p>
    <p><strong>Адрес: </strong>{{contact.address}}</p>
  </div>
      </div>
    </div>
  </section>
</template>

<script>
import axios from "axios"

export default {
  data(){
    return{
      contacts:[],
    }
  },

  mounted(){
    document.title = "Контакты | DoveCuments";
    this.getContacts()
  },
  methods: {
    getContacts(){
      axios
      .get('api/v1/contacts/')
      .then(response => {
        this.contacts = response.data
      })
      .catch(error => {
        console.log(error)
      })
    }
  },
}
</script>

<style lang="scss">


</style>