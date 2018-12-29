<template>
    
    <b-card title="Login" class="col-md-6 mx-auto mt-5">
        <div class="card-text">

            <b-form @submit.prevent="login" novalidate>
                <b-form-group id="loginEmail"
                                label="Email:"
                                label-for="loginEmailInput">
                    <b-form-input id="loginEmailInput"
                                type="email"
                                v-model="form.email"
                                :state="state.email"
                                required
                                placeholder="Enter email">
                    </b-form-input>
                </b-form-group>

                <b-form-group id="loginPassword"
                                label="Password:"
                                label-for="loginPasswordInput">
                    <b-form-input id="loginPasswordInput"
                                type="password"
                                v-model="form.password"
                                :state="state.password"
                                required
                                placeholder="Enter password">
                    </b-form-input>
                </b-form-group>
               
                <b-button type="submit" variant="primary">Login</b-button>
            </b-form>

        </div>
    </b-card>

</template>

<script>
import { mapActions } from 'vuex'

export default {
    data () {
        return {
            form: {
                email: '',
                password: '',
            },
            state: {
                email: null,
                password: null
            }
        }
    },

    methods: {
        ...mapActions([
            'loginUser'
        ]),

        validate() {
            console.log(this.form)
            let ok = true
            // reset init status
            this.state = {
                email: null,
                password: null,
            }

            if (this.form.email === '') {
                ok = false
                this.state.email = false
            }
            console.log('valid email: ', this.validateEmail(this.form.email))
            if (!this.validateEmail(this.form.email)) {
                ok = false
                this.state.email = false
            }
            if (this.form.password === '') {
                ok = false
                this.state.password = false
            }

            // ... add other later, maybe

            return ok
        },

        validateEmail(email) { 
            const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        },

        login() {
            if (this.validate()) {
                this.loginUser()
                this.$router.push({name: 'profile'})
            }
        }
    }
}
</script>

