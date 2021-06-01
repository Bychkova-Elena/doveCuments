<template>
  <div id="wrapper">
    <nav class="navbar p-4 is-info">
      <div class="navbar-brand">
        <router-link to="/" class=" hov navbar-item is-size-4"><strong>DoveCuments</strong></router-link>
        <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu=!showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          </a>
        </div>

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-start">
          <router-link to="/" class="navbar-item">Главная</router-link>
          <router-link to="/courier" class="navbar-item">Курьерам</router-link>
          <router-link to="/tariffs" class="navbar-item">Тарифы</router-link>
          <router-link to="/contacts" class="navbar-item">Контакты</router-link>
          </div>
          <div class="navbar-item navbar-end">
            <div class="buttons">
              <router-link to="/order-form" class="button is-rounded is-warning is-outlined">Заказать доставку</router-link>
              <router-link to="/log-in" class="button is-rounded is-warning">Вход/Регистрация</router-link>
            </div>
          </div>
          </div>
      </nav>

  <router-view/>

  <footer class="footer">
  <div class="is-flex is-align-items-center is-justify-content-space-evenly">
  <div class="content" v-for = "contact in contacts" :key="contact.id">
    <p><strong>{{contact.phone}}</strong></p>
    <p>{{contact.email}}</p>
    <p>{{contact.address}}</p>
  </div>
  <div class="menu">
  <ul class="menu-list">
    <li><router-link to="/order-form" class="navbar-item">Заказать доставку</router-link></li>
    <router-link to="/courier" class="navbar-item">Курьерам</router-link>
    <router-link to="/tariffs" class="navbar-item">Тарифы</router-link>
    <router-link to="/contacts" class="navbar-item">Контакты</router-link>
  </ul>
  </div>
  </div>
  </footer>
  </div>
</template>

<script>
import axios from "axios"

export default {
  data(){
    return{
      showMobileMenu: false,
      contacts:[],
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
    const token = this.$store.state.token
    if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
    } else {
        axios.defaults.headers.common['Authorization'] = ""
    }
  },
  mounted(){
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
@import '../node_modules/bulma';

</style>
