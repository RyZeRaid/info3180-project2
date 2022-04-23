<script>
    import ViewCar from '@/components/ViewCar.vue'

    export default {
    data() {
        return {
            csrf_token: '',

        };
    },
    components: { ViewCar }
}
</script>

<template>
        <ViewCar/>
</template>