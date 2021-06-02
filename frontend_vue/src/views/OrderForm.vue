<template>
<section class="section">
   <div class="columns">
     <div class="column is-6 is-offset-3">
<h1 class="title">Заказ курьерской доставки документов</h1>
<form @submit.prevent="submitForm">
<div class="field">
  <label>Вид доставки: <span class="has-text-danger">*</span></label>
  <div class="control ">
    <div class="select">
      <select v-model="form.delivery">
        <option v-for="delivery in deliveries" :key="delivery.id" :value="delivery.id">{{delivery.name}}</option>
      </select>
    </div>
  </div>
</div>

<div class="field">
  <label>Вес доставки: <span class="has-text-danger">*</span></label>
  <div class="control">
    <div class="select">
      <select v-model="form.weight">
        <option v-for="weight in weights" :key="weight.id" :value="weight.id">{{weight.weight}}</option>
      </select>
    </div>
  </div>
</div>


<div class="field is-grouped is-flex is-flex-direction-column has-background-warning p-6">
  <label class="label">Откуда</label>
  <div class="control">
  <label>Адрес: <span class="has-text-danger">*</span></label>
    <input class="input" type="text" placeholder="Адрес" v-model="form.sendersAddress">
  </div>
    <div class="control">
    <label>ФИО: <span class="has-text-danger">*</span></label>
    <input class="input" type="text" placeholder="ФИО отправителя" v-model="form.sendersFio">
  </div>
    <div class="control">
    <label>Телефон: <span class="has-text-danger">*</span></label>
    <input class="input" type="tel" v-model="form.sendersPhone"  placeholder="Телефон">
  </div>
        <div class="control">
        <label>Дата и время:</label>
    <input class="input" type="datetime-local" v-model="form.sendersDate">
  </div>
</div>

<div class="field is-grouped is-flex is-flex-direction-column has-background-warning p-6">
  <label class="label">Куда</label>
  <div class="control">
  <label>Адрес: <span class="has-text-danger">*</span></label>
    <input class="input" type="text" placeholder="Адрес" v-model="form.recipientAddress">
  </div>
    <div class="control">
    <label>ФИО: <span class="has-text-danger">*</span></label>
    <input class="input" type="text" placeholder="ФИО получателя" v-model="form.recipientFio">
  </div>
    <div class="control">
    <label>Телефон: <span class="has-text-danger">*</span></label>
    <input class="input" type="tel" placeholder="Телефон" v-model="form.recipientPhone">
  </div>
        <div class="control">
        <label>Дата и время:</label>
    <input class="input" type="datetime-local" v-model="form.recipientDate">
  </div>
</div>

<div class="field">
  <label>Способ оплаты: <span class="has-text-danger">*</span></label>
  <div class="control">
    <div class="select">
      <select v-model="form.payment">
        <option v-for="payment in payments" :key="payment.id" :value="payment.id">{{payment.name}}</option>
      </select>
    </div>
  </div>
</div>

<div class="field">
  <label>Ценность отправления, p</label>
  <div class="control">
    <input class="input" type="number" placeholder="0" v-model="form.value">
  </div>
</div>

<div class="field">
  <label>Комментарий:</label>
  <div class="control">
    <textarea class="textarea" placeholder="Комментарий" v-model="form.comment"></textarea>
  </div>
</div>

<div class="field">
  <p class="mb-3"><span class="has-text-danger">*</span> - Поля, обязательные для заполнения</p>
  <label class="label mb-3">Итого: {{form.price}}</label>
  <div class="control">
    <button v-on:click="submit()" class="button is-link">Заказать</button>
  </div>
</div>
</form>
  </div>
</div>
</section>
</template>


<script>
import axios from "axios";

export default {
data() {
    return {
      payments: [],
      deliveries: [], 
      weights:[],

      form: {
                delivery: 0,
                weight: 0,
                sendersAddress: '',
                sendersPhone: '',
                sendersFio: '',
                sendersDate: '', 
                recipientAddress: '',
                recipientPhone: '',
                recipientFio: '',
                recipientDate: '',
                price: 0,
                comment: '',
                value: 0,
                payment: 0
            }
    };
  },
  mounted() {
    document.title = 'Заказ доставки | DoveCuments'
    this.getPayments(), this.getDeliveries(), this.getWeight();
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

    getWeight(){
      axios
        .get("api/v1/weight/")
        .then(response => {
          this.weights = response.data;
        })
        .catch(error => {
          console.log(error);
        });
  },

   submit(){
     console.log(this.form);
            axios
                .post("api/v1/orders/", this.form)
                .then((res) => {
                  console.log(this.form);
                     //Perform Success Action
                 })
                 .catch((error) => {
                     console.log(error);
                 })
                 .finally(() => {
                     //Perform action in always
                 });
        }
}
}
</script>
<style lang="scss" scoped>

</style>