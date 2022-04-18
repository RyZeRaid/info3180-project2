<script>
import RegisterForm from '@/components/RegisterForm.vue'

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
            location: '',
            message: "Hello World! This is Register page"
        };
    },
    components: { RegisterForm }
}
</script>

<template>
    <div class="container">
      <div class="text-center">
        <img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />
        <h1>{{ message }}</h1>
        <RegisterForm/>
      </div>
    </div>
</template>

<style>
/* Add any component specific styles here */
</style>