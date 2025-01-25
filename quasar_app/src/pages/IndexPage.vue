<template>
  <div class="flex justify-between items-center p-4 bg-gray-100 border-b border-gray-300">
    <!-- Left: App Title -->
    <div class="text-xl font-bold text-blue-600">Deployement</div>

    <div class="flex items-center gap-4">
      <span class="text-base">{{ userstore.session.email }}</span>
      <q-btn outline @click="handleLogout" label="Logout" no-caps />
    </div>
  </div>
</template>

<script>
import { defineComponent,ref } from 'vue';
import { useUserStore } from '../stores/user_store';

const userstore = useUserStore();

export default defineComponent({
  name: 'IndexPage',
  setup() {
    return {
      userstore: ref(userstore),

    }
  },
  methods: {
    handleLogout() {
      this.$api.get('/logout')
      .then((res)=>{
        if(res.data.ok){
          this.userstore.clearSession()
          this.$router.push('/login')
        }
      })
    }
  }
});
</script>
