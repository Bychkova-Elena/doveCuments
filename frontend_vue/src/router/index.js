import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'
import OrderForm from '../views/OrderForm.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import MyOrders from '../views/MyOrders.vue'
import Tariffs from '../views/Tariffs.vue'
import Courier from '../views/Courier.vue'
import Contacts from '../views/Contacts.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
    {
    path: '/tariffs',
    name: 'Tariffs',
    component: Tariffs
  },
      {
    path: '/courier',
    name: 'Courier',
    component: Courier
  },
      {
    path: '/contacts',
    name: 'Contacts',
    component: Contacts
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
    {
    path: '/order-form',
    name: 'OrderForm',
    component: OrderForm
  },
        {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
            {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
            {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true,
    },
              children: [
                {
                  path: '/orders',
                  name: "MyOrders",
                  component: MyOrders
                },

      ]
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
