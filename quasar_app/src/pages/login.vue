<template>
  <div class="bg-gray-100 flex items-center justify-center h-screen w-screen">
    <div class="bg-white p-6 rounded-lg shadow-lg w-full max-w-md">
      <h4 class="text-2xl font-bold text-center mb-6">Login</h4>
      <q-form @submit="handleLogin">
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
          hint="Enter your password"
          type="password"
          :rules="[rules.required, rules.password]"
          class="mb-4"
          dense
        />

        <!-- Login Button -->
        <div class="flex justify-center">

            <q-btn
            label="Login"
            type="submit"
            color="primary"
            class="w-full mt-4"
            unelevated
            />
        </div>

        <!-- Signup Redirect Button -->
        <div class="flex justify-center mt-4">
          <q-btn
            label="New here? Signup"
            flat
            color="secondary"
            @click="$router.push('/register')" 
          />
        </div>
      </q-form>
    </div>
  </div>
</template>

<script>
import { defineComponent,ref } from 'vue';

export default defineComponent({
  name: 'LoginPage',
  setup() {
    return {
        form:ref({
            email:'',
            password:''
        })
    }
  },
  computed: {
    rules() {
      return {
        required: (val) => !!val || 'This field is required',
        email: (val) =>
          /^\S+@\S+\.\S+$/.test(val) || 'Enter a valid email address',
        password: (val) =>
          (val.length >= 6 &&
            /[!@#$%^&*(),.?":{}|<>]/.test(val) &&
            !/\s/.test(val)) ||
          'Password must be at least 6 characters, include 1 special character, and have no spaces',
      };
    },
  },
  methods: {
    handleLogin() {
      // Here you can handle the login logic, for example, authentication with an API.
      console.log('Login successful for:', this.form.email);

      this.$api.get("/login")
      .then((res)=>{
        console.log(res.data.message)
      })

      // Clear the form after successful login (or you could navigate to a new page)
      this.form.email = '';
      this.form.password = '';
    },
  },
});
</script>

<style scoped>
/* Add any additional styles here if necessary */
</style>
