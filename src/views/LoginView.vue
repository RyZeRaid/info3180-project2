<script>
import LoginForm from '@/components/LoginForm.vue'

export default {
    data() {
        return {
           
            token: '',
            message: "Hello World! This is login page"
        };
    },
    components: { LoginForm }
}
</script>

<template>
    <div class="container">
      <div class="text-center">
        
        <h1>{{ message }}</h1>
        <p>this is the token : {{ token }}</p>
        <LoginForm/>
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
</style>