<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary fixed-top" :key="$route.fullPath">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">Lab 7</a>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarSupportedContent"
          aria-controls="navbarSupportedContent"
          aria-expanded="false"
          aria-label="Toggle navigation"
          
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent" :key="$route.fullPath"> 
          <ul class="navbar-nav me-auto" id = "nav">
            <li class="nav-item">
              <RouterLink to="/" class="nav-link active" >Home</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/about">About</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/register">Register</RouterLink>
            </li>
            <div v-if = "check === 'null' " >
              <li class="nav-item">
                
                <RouterLink class="nav-link" to="/login">Login</RouterLink>
              </li>
            </div>
            <div v-else>
                <li class="nav-item">
                  
                <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
                </li>
            </div>
          </ul>
        </div>
      </div>
    </nav>
  </header>
</template>

<script>
import { RouterLink } from "vue-router";

export default {
    data() {
        return {
             check : localStorage.getItem('id')
            
        };
    },
    
}
</script>

<style>
/* Add any component specific styles here */
</style>