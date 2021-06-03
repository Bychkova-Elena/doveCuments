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
        <option value="0" selected>Выберите вид доставки</option>
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
        <option value="0" selected>Выберите вес документов</option>
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
        <option value="0" selected>Выберите способ оплаты</option>
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

  <div class="notification is-danger" v-if="errors.length">
  <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
  </div>

<div class="field">
  <p class="mb-3"><span class="has-text-danger">*</span> - Поля, обязательные для заполнения</p>
  <label class="label mb-3">Итого: {{totalPrice}}</label>
  <div class="control">
    <button class="button is-link">Заказать</button>
  </div>
</div>
</form>
  </div>
</div>
</section>
</template>


<script>
import axios from "axios";
import {toast} from "bulma-toast";

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
                sendersDate: null, 
                recipientAddress: '',
                recipientPhone: '',
                recipientFio: '',
                recipientDate: null,
                price: 100,
                comment: '',
                value: 0,
                payment: 0
            },
            errors: []
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


      async submitForm() {
            this.errors = []
            if (this.form.delivery === 0) {
                this.errors.push('Не указан способ доставки!')
            }
            if (this.form.weight === 0) {
                this.errors.push('Не указан вес документов!')
            }
            if (this.form.sendersAddress === '') {
                this.errors.push('Не указан адрес отправителя!')
            }
            if (this.form.sendersPhone === '') {
                this.errors.push('Не указан телефон отправителя!')
            }
            if (this.form.sendersFio === '') {
                this.errors.push('Не указано фио отправителя!')
            }
            if (this.form.recipientAddress === '') {
                this.errors.push('Не указан адрес получателя!')
            }
            if (this.form.recipientPhone === '') {
                this.errors.push('Не указан телефон получателя!')
            }
            if (this.form.recipientFio === '') {
                this.errors.push('Не указано фио получателя!')
            }
            if (this.form.payment === '') {
                this.errors.push('Не указан способ оплаты!')
            }
            if (!this.errors.length) {
              
              const data = {
                'user':null,
                'delivery': this.form.delivery,
                'weight': this.form.weight,
                'sendersAddress': this.form.sendersAddress,
                'sendersPhone': this.form.sendersPhone,
                'sendersFio': this.form.sendersFio,
                'sendersDate': this.form.sendersDate,
                'recipientAddress': this.form.recipientAddress,
                'recipientPhone': this.form.recipientPhone,
                'recipientFio': this.form.recipientFio,
                'recipientDate': this.form.recipientDate,
                'payment': this.form.payment,
                'value': this.form.value,
                'comment': this.form.comment,
                'price': this.form.price
            }

          await axios
                .post('/api/v1/create-orders/', data)
                .then(response => {
                    this.$router.push('/');
                    toast({
                            message: 'Заказ успешно создан!',
                            type: 'is-success',
                            dismissible: true,
                            pauseOnHover: true,
                            duration: 2000,
                            position: 'bottom-right',
                        })
                })
                .catch(error => {
                    this.errors.push('Что-то пошло не так. Попробуйте ещё раз.')
                    console.log(error)
                })
      }
  },
},

computed: {
      totalPrice() {
            this.form.price = 100+ parseInt(this.form.value)
            // if (this.form.delivery !== 0){
            //   this.form.price += parseInt(this.deliveries[1].price);
            // }
            // if (this.form.weight !== 0){
            //   this.form.price += parseInt(this.weights[1].price);
            // }
            return this.form.price;
        }, 
    }
}
</script>
<style lang="scss" scoped>
select{
  width:50rem;
}
</style>