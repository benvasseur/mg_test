import Router from 'vue-router';

import home from './content/home.vue';
import profile from './content/profile.vue';
import register from './content/register.vue';
import login from './content/login.vue';
import store from './store'


const routes = [
    { 
        path: '/', 
        alias: '/home',
        name: 'home', 
        component: home 
    },
    { 
        path: '/register',
        name: 'register', 
        component: register,
        beforeEnter: (to, from, next) => {
            console.log('is logged in ', store.getters.isLoggedIn)
            if (store.getters.isLoggedIn) {
                next({ name: 'profile'})
            }
            else {
                next()
            }
        }
    },
    { 
        path: '/login',
        name: 'login', 
        component: login,
        beforeEnter: (to, from, next) => {
            console.log('is logged in ', store.getters.isLoggedIn)
            if (store.getters.isLoggedIn) {
                next({ name: 'profile'})
            }
            else {
                next()
            }
        }
    },
    { 
        path: '/profile',
        name: 'profile', 
        component: profile,
        beforeEnter: (to, from, next) => {
            console.log('is logged in ', store.getters.isLoggedIn)
            if (store.getters.isLoggedIn) {
                next()
            }
            else {
                next({ name: 'login'})
            }
        }
    },
  ]

export default new Router({
  mode: 'history',
  routes
});
