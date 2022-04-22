<template>
        <div class="login-form center-block">
    <h2 class="h3 mb-3 fw-normal">Please Log in</h2>
    
    <form id = "LoginForm" >
 
        <div class="col-auto">
        <div class="form-group">
            <label for="username">username</label>
            <input name="username" v-model="username" placeholder="username">
            </div>
        </div>
        <div class="col-auto">
        <div class="form-group">
            <label for="password">password</label>
            <input name="password" v-model="password" placeholder="password" type="password">
            </div>
        </div>
        
      <button type="submit" name="submit" class="btn btn-primary btn-block" @click.prevent= "login">Log in</button>
    
    </form>
  </div>
</template>

<script>
import store from '@/main.js'; 

export default {
    data() {
        return {
          csrf_token: '',
          username: '',
          password: '',
         
        };
    },
    created() {
        this.getCsrfToken();
       
    },
  methods: {
    login(){
      console.log("came in function")
      let loginForm = document.getElementById('LoginForm');
      let form_data = new FormData(loginForm);
        fetch("/api/auth/login", {
            method: 'POST', 
            body: form_data,
            headers: {'X-CSRFToken': this.csrf_token}
          })
          .then(function (response) {
                console.log(response)
                return response.json();
              
          })
          .then(function (data) {
          // display a success message
            if(data.token != ''){
                
                localStorage.setItem('token', data.token )
                localStorage.setItem('id', data.id )
                store.commit('checktrue', true);
            }else{
                
                localStorage.setItem('token', null )
                localStorage.setItem('id', null )
                store.commit('checktrue', false);
            }
            
            localStorage.setItem('auth', data.auth )
            
            
            console.log("show me the check :", store.state.check)
            console.log("this is the token in local storage",localStorage.getItem('id'))
            console.log(data.token, data.id,localStorage.getItem('auth') );
            
            return(data);
          })
          .catch(function (error) {
              console.log(error);
          });
          
          this.$router.push('/');
          
    },
    getCsrfToken(){
      console.log("thisis the state when logged",this.$store.state.auth)
      let self = this;
      fetch('/api/csrf-token')
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          self.csrf_token = data.csrf_token;
        })
    },
   
  }  
}
</script>

<style>
/* Add any component specific styles here */
</style>