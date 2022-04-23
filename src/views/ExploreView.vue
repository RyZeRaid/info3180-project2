<script>
import Explore from '@/components/Explore.vue'

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
            message: "Hello World! This is Explore page"
        };
    },
    components: { Explore }
}
</script>

<template>
    <div class="container">
        <Explore/>
      </div>
</template>

<style>
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

body {
  background-color: #f3f4f6;
}
</style>