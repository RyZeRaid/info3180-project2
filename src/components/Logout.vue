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

export default {
     
    watch:{
        '$store'(to , from){
            alert(to.auth);
        }
    }, 
    created() {
        this.logout();
       
    },
  methods: {
    logout(){
        
    },

  }  
}
</script>

<style>
/* Add any component specific styles here */
</style>