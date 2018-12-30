import Vue from 'vue'
import Vuex from 'vuex'
import api from '../api'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        userId: null,
        userName: null,
        userEmail: null,
        userPicture: null,
        userToken: null
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
        getUserToken(state){
            return state.userToken
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
            if (user.token) {
                state.userToken = user.token;
            }
        },
        removeUser(state) {
            state.userId = null
            state.userName= null
            state.userEmail= null
            state.userPicture= null
            state.userToken= null        }
    },
    actions: {
        async registerUser ({ commit }, data) {
            const response = await api.register(data)
            console.log('response', response)

            const user = response.data.user
            user.token = response.data.token 

            commit('setUser', user)
        },
        async loginUser ({ commit }, credentials) {
            const response = await api.login(credentials)
            console.log('response', response)

            const user = response.data.user
            user.token = response.data.token

            commit('setUser', user)
        },
        async updateUser ({ commit, state }, data) {
            const response = await api.update(state.userId, data)
            console.log('response', response)

            const user = response.data

            commit('setUser', user)
        },
        logoutUser ({ commit }) {
            commit('removeUser')
        }
    },
    plugins: [createPersistedState()]
})