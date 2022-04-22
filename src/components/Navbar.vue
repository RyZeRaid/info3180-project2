<template>
  <header>
    <nav class="navbar navbar-expand-lg navbar-dark fixed-top" :key="$route.fullPath">
      <div class="container-fluid">
        <RouterLink class="navbar-brand" to="/"><fa icon="car" /> United Auto Sales</RouterLink>
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
              <RouterLink class="nav-link" to="/explore">Explore</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link" to="/addcar">Add Car</RouterLink>
            </li>
              <li class="nav-item">
                
                <RouterLink class="nav-link" to="/logout">Logout</RouterLink>
              </li>               
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
  nav{
    background-color: #202938;
  }
</style>