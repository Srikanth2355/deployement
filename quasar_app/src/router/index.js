import { defineRouter } from '#q-app/wrappers'
import { createRouter, createMemoryHistory, createWebHistory, createWebHashHistory } from 'vue-router'
import routes from './routes.js'
import { defineStore } from 'pinia'
import { useUserStore } from '../stores/user_store.js'
import axios from 'axios'

/*
 * If not building with SSR mode, you can
 * directly export the Router instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Router instance.
 */
// const userStore = useUserStore();

export default defineRouter(function (/* { store, ssrContext } */) {
  const createHistory = process.env.SERVER
    ? createMemoryHistory
    : (process.env.VUE_ROUTER_MODE === 'history' ? createWebHistory : createWebHashHistory)

  const Router = createRouter({
    scrollBehavior: () => ({ left: 0, top: 0 }),
    routes,

    // Leave this as is and make changes in quasar.conf.js instead!
    // quasar.conf.js -> build -> vueRouterMode
    // quasar.conf.js -> build -> publicPath
    history: createHistory(process.env.VUE_ROUTER_BASE)
  })

  Router.beforeEach(async (to, from, next) => {
    const userStore = useUserStore();
    if(to.path == '/login' || to.path == '/register'){
      try {
        const response = await axios.get('/api/is_logged_in')
        if(response.data.ok){
          userStore.setSession(response.data.user)
          next('/')
        }else{
          console.log("user not logged in")
          next()
        }
      }catch(e){
        console.log(e)
        next()
      }
    }else{
      try{
        const response = await axios.get('/api/is_logged_in')
        if(response.data.ok){
          userStore.setSession(response.data.user)
          next()
        }else{
          userStore.clearSession()
          next('/login')
        }
      }catch(e){
        console.log(e)
        userStore.clearSession()
        next('/login')
      }
    }
  })
  return Router
})


