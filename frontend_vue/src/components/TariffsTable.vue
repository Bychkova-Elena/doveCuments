<template>
<div>
          <div class="table-container is-flex">
  <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
    <thead>
    <tr>
      <th>Способ доставки</th>
      <th>Цена</th>
    </tr>
  </thead>
  <tbody v-for="delivery in deliveries" :key="delivery.id">
    <tr>
      <td>
    <label class="radio">
    <input type="radio" name="delivery" :value="delivery.price" v-model="deliveryPrice">
        {{delivery.name}}
      </label>
        </td>
      <td>{{delivery.price}}</td>
  </tr>
  </tbody>
  </table>
   <table class="table is-bordered is-striped is-narrow is-hoverable is-fullwidth">
    <thead>
    <tr>
      <th>Вес</th>
      <th>Цена</th>
    </tr>
  </thead>
  <tbody v-for="weight in weights" :key="weight.id">
    <tr>
      <td>
    <label class="radio">
    <input type="radio" name="weight" :value="weight.price" v-model="weightPrice">
        {{weight.weight}}
      </label>
        </td>
      <td>{{weight.price}}</td>
    </tr>
  </tbody>
  </table>
</div>
 <h2 class="has-text-right"><b>Итого: </b> {{totalPrice}} + цена за адрес </h2>
 </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      deliveries: [], 
      weights:[],
      deliveryPrice:0,
      weightPrice:0
    };
  },
  mounted() {
    this.getDeliveries(), this.getWeight();
  },
  methods: {
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

    getWeight() {
      axios
        .get("api/v1/weight/")
        .then((response) => {
          this.weights = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  computed: {
    totalPrice() {
      return this.deliveryPrice + this.weightPrice;
    }
  }
};
</script>

<style lang="scss" scoped>
</style>
