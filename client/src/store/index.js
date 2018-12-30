import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        userId: null,
        userName: null,
        userEmail: null,
        userPicture: null
        // userId: 1,
        // userName: 'Benjamin',
        // userEmail: 'benvasseur59@gmail.com',
        // userPicture: 'https://avatars3.githubusercontent.com/u/46235560?s=400&u=82b48466224450807786b1461dd8010a86ed7cde&v=4',
    },
    getters: {
        isLoggedIn(state){
            return !!state.userId
        },
        getUserName(state){
            return state.userName
        },
        getUserEmail(state){
            return state.userEmail
        },
        getUserPicture(state){
            return state.userPicture
        }
    },
    mutations: {
        setUser(state, user) {
            if (user.id) {
                state.userId = user.id;
            }
            if (user.name) {
                state.userName = user.name;
            }
            if (user.email) {
                state.userEmail = user.email;
            }
        },
        removeUserId(state) {
            state.userId = null;
        }
    },
    actions: {
        async registerUser ({ commit }) {
            return new Promise((resolve, reject) => {
                // call register api...
                const user = {
                    id: 1,
                    name: 'Benjamin',
                    email: 'benvasseur59@gmail.com',
                }
                commit('setUser', user)
            })
        },
        async loginUser ({ commit }) {
            await api.login({
                email: 'benvasseur59@gmail.com',
                password: '123'
            })

            const user = {
                id: 1,
                name: 'Benjamin',
                email: 'benvasseur59@gmail.com',
            }
            commit('setUser', user)
            
            return user
        },
        async updateUser ({ commit }) {
            return new Promise((resolve, reject) => {
                // call update api...
                const user = {
                    id: 1,
                    name: 'Benjamin2',
                    email: 'benvasseur59@gmail.com',
                }
                commit('setUser', user)
            })
        },
        logoutUser ({ commit }) {
            return new Promise((resolve, reject) => {
                // call login api...
                commit('removeUserId')
            })
        }
    }
})