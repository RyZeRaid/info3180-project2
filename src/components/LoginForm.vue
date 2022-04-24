<template>

<div class="login">

<h2 class="page-header" id="pgheader">Login to your account</h2>

<div class="card text-left" style="width: 40rem; " id = "card">
<div class="card-body">
  
    
    <form id = "LoginForm" >
 
        <div class="col-auto">
        <div class="form-group">
            <label for="username">Username</label>
            <input class="form-control" name="username" v-model="username" placeholder="Username">
            </div>
        </div>
        <div class="col-auto">
        <div class="form-group">
            <label for="password">Password</label>
            <input class="form-control" name="password" v-model="password" placeholder="Password" type="password">
            </div>
        </div>
        <br>
      <button type="submit" name="submit" class="btn btn-primary btn-block" @click.prevent= "login">Log in</button>
    
    </form>
  </div>
</div>
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
                
                localStorage.setItem('token', data.token );
                localStorage.setItem('id', data.id);
                store.commit('checktrue', true);
                store.commit('checkid', data.id );
                store.commit('addcount');
            }else{
                
                localStorage.setItem('token', null );
                localStorage.setItem('id', null );
                store.commit('checktrue', false);
            }
            
            localStorage.setItem('auth', data.auth );
          
            return(data);
          })
          .catch(function (error) {
              console.log(error);
          });
          
          this.$router.push('/explore');
          
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

.page-header{
  font-size: 2em;
}

label {
    font-weight: bold;
    font-size: 0.8em;
  }

.login{
  margin-top: 10rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>