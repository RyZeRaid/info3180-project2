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
        <LoginForm/>
      </div>
    </div>
</template>

<style>
body {
  background-color: #f3f4f6;
}
</style>