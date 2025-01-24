<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    >
  <p class="text-h1 text-red-600">sdvsff {{ userstore.session.name }}</p>
  <q-btn @click="setsession">set session</q-btn>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue';
import { useUserStore } from 'src/stores/user_store';

const userstore = useUserStore();

export default defineComponent({
  name: 'IndexPage',
  setup() {
    return {
      userstore: userstore,

    }
  },
  methods: {
    setsession() {
      this.userstore.setSession({name: 'srikanth Gubba', email: 'srikanth@incentius.com', id: '123', role: 'user'})
    }
  }
});
</script>
