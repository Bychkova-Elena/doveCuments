import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import OrderForm from '../views/OrderForm.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
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
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
