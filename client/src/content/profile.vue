<template>
    <div>
        <div class="position-fixed w-100" v-if="dismissCountDown>0">
            <b-alert variant="success"
                    class="col-lg-4 col-md-6 col-sm-8 mx-auto mt-3"
                    dismissible
                    :show="dismissCountDown"
                    fade
                    @dismissed="showDismissibleAlert=false"
                    @dismiss-count-down="countDownChanged">
                Profile updated
            </b-alert>
        </div>

        <b-jumbotron :header="title" class="text-center" fluid>
        </b-jumbotron>

        <b-card title="Update user profile" class="col-lg-4 col-md-6 col-sm-8 mx-auto mt-5">
            <div class="card-text">

                <b-form @submit.prevent="update" novalidate>
                    <b-img 
                        v-if="getUserPicture"
                        rounded="circle" 
                        :src="getUserPicture"
                        thumbnail 
                        fluid
                        width="150" 
                        height="150" 
                        alt="thumb" 
                        class="m-1" />
                    <b-form-group id="updateName">
                        <b-form-file v-model="form.file" 
                            id="updateFileInput"
                            plain
                            placeholder="Choose a profile picture"></b-form-file>
                    </b-form-group>
                    
                    <b-form-group id="updateName"
                                    label="Name:"
                                    label-for="updateNameInput">
                        <b-form-input id="updateNameInput"
                                    type="text"
                                    v-model="form.name"
                                    :state="state.name"
                                    required
                                    placeholder="Enter full name">
                        </b-form-input>
                    </b-form-group>

                    <b-form-group id="updateEmail"
                                    label="Email:"
                                    label-for="updateEmailInput">
                        <b-form-input id="updateEmailInput"
                                    type="email"
                                    v-model="form.email"
                                    :state="state.email"
                                    required
                                    placeholder="Enter email">
                        </b-form-input>
                    </b-form-group>
                
                    <b-button type="submit" variant="primary">Update</b-button>
                </b-form>

            </div>
        </b-card>
    </div>
    
</template>

<script>
import { mapGetters, mapActions } from 'vuex'

export default {
    data () {
        return {
            form: {
                file: null,
                name: '',
                email: ''
            },
            state: {
                name: null,
                email: null
            },
            dismissSecs: 5,
            dismissCountDown: 0
        }
    },

    computed: {
        ...mapGetters([
            'getUserName',
            'getUserEmail',
            'getUserPicture'
        ]),

        title: function () {
            return `${this.getUserName}'s profile`
        }
    },

    methods: {
        ...mapActions([
            'updateUser'
        ]),

        init() {
            this.form.name = this.getUserName
            this.form.email = this.getUserEmail
        },

        validate() {
            console.log(this.form)
            let ok = true
            // reset init status
            this.state = {
                name: null,
                email: null
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

            // ... add other later, maybe

            return ok
        },

        validateEmail(email) { 
            const re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            return re.test(String(email).toLowerCase());
        },

        showAlert () {
            this.dismissCountDown = this.dismissSecs
        },

        countDownChanged (dismissCountDown) {
            this.dismissCountDown = dismissCountDown
        },

        async update() {
            if (this.validate()) {
                await this.updateUser(this.form)
                this.init()
                this.showAlert()
            }
        }
    },

    mounted() {
        this.init()
    }
}
</script>

