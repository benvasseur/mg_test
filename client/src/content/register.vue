<template>
    <b-card title="Register" class="col-md-6 mx-auto mt-5">
        <div class="card-text">

            <b-form @submit.prevent="register" novalidate>
                <b-form-group id="registerName"
                                label="Name:"
                                label-for="registerNameInput">
                    <b-form-input id="registerName"
                                type="text"
                                v-model="form.name"
                                :state="state.name"
                                required
                                placeholder="Enter full name">
                    </b-form-input>
                </b-form-group>

                <b-form-group id="registerEmail"
                                label="Email:"
                                label-for="registerEmailInput">
                    <b-form-input id="registerEmailInput"
                                type="email"
                                v-model="form.email"
                                :state="state.email"
                                required
                                placeholder="Enter email">
                    </b-form-input>
                </b-form-group>

                <b-form-group id="registerPassword"
                                label="Password:"
                                label-for="registerPasswordInput">
                    <b-form-input id="registerPasswordInput"
                                type="password"
                                v-model="form.password"
                                :state="state.password"
                                required
                                placeholder="Enter password">
                    </b-form-input>
                </b-form-group>

                <b-form-group id="registerPasswordConfirmation"
                                label="Password:"
                                label-for="registerPasswordInputConfirmation">
                    <b-form-input id="registerPasswordInputConfirmation"
                                type="password"
                                v-model="form.passwordConfirmation"
                                :state="state.passwordConfirmation"
                                required
                                placeholder="Confirm password">
                    </b-form-input>
                </b-form-group>
               
                <b-button type="submit" variant="primary">Register</b-button>
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
                name: '',
                email: '',
                password: '',
                passwordConfirmation: '',
            },
            state: {
                name: null,
                email: null,
                password: null,
                passwordConfirmation: null,
            }
        }
    },

    methods: {
        ...mapActions([
            'registerUser'
        ]),

        validate() {
            console.log(this.form)
            let ok = true
            // reset init status
            this.state = {
                name: null,
                email: null,
                password: null,
                passwordConfirmation: null,
            }

            if (this.form.name === '') {
                ok = false
                this.state.name = false
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
            if (this.form.passwordConfirmation === '') {
                ok = false
                this.state.passwordConfirmation = false
            }
            if (this.form.passwordConfirmation !== this.form.password) {
                ok = false
                this.state.password = false
                this.state.passwordConfirmation = false
            }

            // ... add other later, maybe

            return ok
        },

        validateEmail(email) { 
            const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        },

        register() {
            if (this.validate()) {
                this.registerUser()
                this.$router.push({name: 'profile'})
            }
        }
    }
}
</script>

