import { createApp } from 'vue'
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import App from './App.vue'
import router from './router'
import { createStore } from 'vuex';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

library.add(fas)

const store = createStore({
    state(){
        return{
            token: localStorage.getItem('token') || null,
            id: localStorage.getItem('id') || null,
            auth: localStorage.getItem('auth') || false
        }
        
    }
});

router.beforeEach((to, from, next) => {
    console.log("came here actually ")
    console.log("this is it", store.state.auth, store.state.id)
    if(to.path === '/register' && store.state.auth === 'false'){
      next('/login')
    }else{
      next()
    }
    if(to.path === '/logout' && store.state.auth === 'true'){
        console.log("was loggged out");
        localStorage.setItem('token', null );
        localStorage.setItem('id', null );
        localStorage.setItem('auth', false );
        next('/');
        window.location.reload();
      }
    
  });
const app = createApp(App)

.component('fa', FontAwesomeIcon)

app.use(router)
app.use(store)

app.mount('#app')
