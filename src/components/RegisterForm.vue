<template>
<h1 class="page-header" id="pgheader">Register New User</h1>

<div class="card text-left" style="width: 48rem; " id = "card">
<div class="card-body">
<form  id = "RegisterForm" >
  
  <div class="row mb-2">
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
  </div>

  <div class="row mb-2">
    <div class="col-auto">
      <div class="form-group">
        <label for="name">Full Name</label>
        <input name="name" v-model="name" placeholder="full name">
        </div>
    </div>
    <div class="col-auto">
      <div class="form-group">
        <label for="email">Email</label>
        <input name="email" v-model="email" placeholder="John.bond764@gmail.com">
        </div>
    </div>
  </div>

    <div class="row mb-1">
        <div class="col-auto">
            <div class="form-group">
                <label for="location">Location</label>
                <input name="location" v-model="location" placeholder="">
            </div>
        </div>
    </div>

    <div class="form-group">
        <label for="description">Biography</label>
        <textarea name="description" v-model="description"
            id="description" class="form-control mb-2 mr-sm-2" placeholder="add a description"></textarea>
    </div>
   
    <div class="form-group">
        <input type="file" id="photo" name="photo" @change="selectImage">
    </div>
  
  <div class="col-12">
    <button type="submit" name="submit" class="btn btn-primary" @click="register">Register</button>
    <button type="reset" name="reset" class="btn btn-warning">Undo all</button>
  </div>
  
</form>
</div>
</div>
</template>

<script>
export default {
    data() {
        return {
          csrf_token: '',
          description: '',
          photo: '',
          email: '',
          name: '',
          username: '',
          password: '',
          location: ''
        }
    },
    created() {
        this.getCsrfToken();
    },
  methods: {
    register(){

      let registerForm = document.getElementById('RegisterForm');
      let form_data = new FormData(registerForm);
        fetch("/api/register", {
            method: 'POST', 
            body: form_data,
            headers: {'X-CSRFToken': this.csrf_token}
          })
          .then(function (response) {
                return response.json();
          })
          .then(function (data) {
          // display a success message
            console.log(data);
          })
          .catch(function (error) {
              console.log(error);
          });
    },
    getCsrfToken(){
      let self = this;
      fetch('/api/csrf-token')
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
          self.csrf_token = data.csrf_token;
        })
    }
  }  
}
</script>

<style>
/* Add any component specific styles here */
</style>