import { defineStore } from 'pinia' 

export const useUserStore = defineStore('user', {
    state: () => ({
        session:{
            name : 'srikanth',
            email:'',
            id: '',
            role: ''
        },
    }),
    actions: {
        setSession(data){
            this.session.email = data.email,
            this.session.name = data.name,
            this.session.id = data.id,
            this.session.role = data.role   
        }
    }
})