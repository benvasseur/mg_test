<template>
    <b-jumbotron :header="title" class="text-center" fluid>
        <b-btn 
            variant="primary" 
            :to="{ name: 'register'}"  
            v-if="!this.isLoggedIn">
            Learn More
        </b-btn>
    </b-jumbotron>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
    computed: {
        ...mapGetters([
            'isLoggedIn',
            'getUserName'
        ]),

        title: function () {
            return this.isLoggedIn ? 
                `Welcome ${this.getUserName} to The Monad` : 
                "Welcome to The Monad guest"
        }
    }
}
</script>

