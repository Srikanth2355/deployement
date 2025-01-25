<template>
  <div class="bg-gray-100 flex items-center justify-center w-screen h-screen">
    <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
      <h4 class="text-2xl font-bold text-center mb-6">Register Form</h4>
      <q-form @submit="handleRegister">
        <!-- Name Input -->
        <q-input
          filled
          v-model="form.name"
          label="Name"
          hint="Enter your full name"
          :rules="[rules.required,rules.noSpacesOnly]"
          class="mb-4"
          dense
        />

        <!-- Email Input -->
        <q-input
          filled
          v-model="form.email"
          label="Email"
          hint="Enter your email address"
          type="email"
          :rules="[rules.required, rules.email]"
          class="mb-4"
          dense
        />

        <!-- Password Input -->
        <q-input
          filled
          v-model="form.password"
          label="Password"
          hint="Minimum 6 characters, 1 special character"
          type="password"
          :rules="[rules.required, rules.password]"
          class="mb-4"
          dense
        />

        <!-- Confirm Password Input -->
        <q-input
          filled
          v-model="form.confirmPassword"
          label="Confirm Password"
          hint="Re-enter your password"
          type="password"
          :rules="[rules.required, rules.matchPassword]"
          class="mb-4"
          dense
        />

        <!-- Register Button -->
        <div class="flex justify-center">

            <q-btn
            label="Register"
            type="submit"
            color="primary"
            class="w-44 mt-4 mb-2"
            unelevated
            />
        </div>
      </q-form>
      <p class="text-center"> Already have an account? <span @click="$router.push('/login')" class="text-blue-600 cursor-pointer">Login</span></p>
    </div>
  </div>
</template>

<script>
import { defineComponent, ref  } from 'vue';
import { useUserStore } from 'src/stores/user_store';

const userstore = useUserStore();

export default defineComponent({
    setup() {
        return {
            form: ref({
                name: '',
                email: '',
                password: '',
                confirmPassword: ''
            }),
        }

    },
    computed: {
        rules(){
            return{
                required: (val) => !!val || 'This field is required',
                noSpacesOnly: (val) =>
        val.trim().length > 0 || 'Please enter a Name',
                email: (val) =>
                    /^\S+@\S+\.\S+$/.test(val) || 'Enter a valid email address',
                password: (val) =>
                    (val.length >= 6 &&
                    /[!@#$%^&*(),.?":{}|<>]/.test(val) &&
                    !/\s/.test(val)) ||
                    'Password must be at least 6 characters, include 1 special character, and have no spaces',
                matchPassword: (val) =>
                    val === this.form.password || 'Passwords do not match',
            }
        }
    },
    methods: {
        handleRegister(){
            this.$q.loading.show()
            
              this.$api.post('/register', this.form)
              .then((res)=>{
                if(res.data.ok){
                  this.$q.loading.hide()
                  this.$q.notify({
                    color: 'positive',
                    message: 'Registration successful'
                  })
                  this.$router.push('/login')
                }
              })

            .catch((err)=>{
              this.$q.loading.hide()
              this.$q.notify({
                color: 'negative',
                message: err.message
              })

            })
        }
    }
})
</script>