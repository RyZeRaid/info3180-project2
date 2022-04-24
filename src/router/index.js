import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),

  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/register',
      name: 'Register',
      component: () => import('../views/RegisterView.vue'),
      
    },
    {
      path: '/login',
      name: 'Login',
      component: () => import('../views/LoginView.vue')
      
    },
    {
      path: '/logout',
      name: 'Logout'
      
    },{
      path: '/explore',
      name: 'Explore',
      component: () => import('../views/ExploreView.vue'),
      props: true
    },
    {
      path: '/addcar',
      name: 'Add New Car',
      component: () => import('../views/NewCarView.vue')
    },
    {
      path: '/cars/:id/:user_id',
      name: 'View Car',
      component: () => import('../views/ViewCarView.vue')
    },
  ]
})



export default router
