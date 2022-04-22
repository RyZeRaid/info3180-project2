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
        <RegisterForm/>
      </div>
</template>

<style>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
</style>