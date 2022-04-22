<script>
import { RouterLink, RouterView } from 'vue-router'
import AppHeader from "@/components/AppHeader.vue";
import Navbar from "@/components/Navbar.vue";
import AppFooter from "@/components/AppFooter.vue";


export default{
    components:{
      Navbar,
      AppHeader
    },created(){
      this.if_reload();
    },
    computed: {
       getConditionallyRenderedNavbar() {
         if (this.$store.state.check){
           return Navbar;
         }else{
           return AppHeader;
         }
          //or second nav or no nav
       }
    },
    methods: {
      if_reload(){
        if(localStorage.getItem('id') !== 'null'){
          this.$store.commit('checktrue', true);
        }
      }
    },
}

</script>

<template>
  <keep-alive>
    <component :is="getConditionallyRenderedNavbar"/>
  </keep-alive>

  <main>
    <RouterView />
  </main>
</template>

<style> 
body {
  padding-top: 75px;
}
</style>
