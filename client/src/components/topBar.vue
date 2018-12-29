<template>
    <b-navbar toggleable="md" type="dark" variant="dark">

        <b-navbar-toggle target="nav_collapse"></b-navbar-toggle>

        <b-navbar-brand :to="{ name: 'home'}">Home</b-navbar-brand>

        <b-collapse is-nav id="nav_collapse">

            <!-- Right aligned nav items -->
            <b-navbar-nav class="ml-auto" v-if="isLoggedIn">
                <b-nav-item :to="{ name: 'profile'}">Profile</b-nav-item>
                <b-nav-item @click="logout">Logout</b-nav-item>
            </b-navbar-nav>

            <b-navbar-nav class="ml-auto" v-else>
                <b-nav-item :to="{ name: 'login'}">Login</b-nav-item>
                <b-nav-item :to="{ name: 'register'}">Register</b-nav-item>
            </b-navbar-nav>

        </b-collapse>
    </b-navbar>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    data () {
        return {

        }
    },

    computed: {
        ...mapGetters([
            'isLoggedIn'
        ])
    },

    methods: {
        ...mapActions([
            'logoutUser'
        ]),

        logout() {
            this.logoutUser()
            this.$router.push({name: 'home'})
        }
    }
}
</script>
