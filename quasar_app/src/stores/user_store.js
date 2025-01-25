import { defineStore } from 'pinia' 

export const useUserStore = defineStore('user', {
    state: () => ({
        session:{
            name : '',
            email:'',
            id: '',
            role: ''
        },
    }),
    actions: {
        setSession(data){
            this.session.email = data['email'],
            this.session.name = data['name'],
            this.session.id = data['id'],
            this.session.role = data['role']   
        },
        clearSession(){
            this.session.email = '',
            this.session.name = '',
            this.session.id = '',
            this.session.role = ''
        }

    }
})