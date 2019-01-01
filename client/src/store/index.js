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
    },
    getters: {
        isLoggedIn(state){
            return !!state.userId
        },
        getUserId(state){
            return state.userId
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
            if (user.profile_picture) {
                state.userPicture = user.profile_picture;
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
        async updateUserProfilePic ({ commit, state }, file) {
            const formData = new FormData();
            formData.append("file", file);

            const response = await api.updateProfilePic(state.userId, formData)
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