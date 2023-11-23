// Composables
import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ArticleView from '@/views/ArticleView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ProfileView from '@/views/ProfileView.vue'
import MovieView from '@/views/MovieView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'




const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes : [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    }, 
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    }, 
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    }, 
    {
      path: '/articles/create/',
      name: 'ArticleCreateView',
      component: ArticleCreateView
    }, 
    {
      path: '/articles/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView
    }, 
    {
      path: '/articles/:id/update/',
      name: 'ArticleUpdateView',
      component: ArticleUpdateView
    }, 
    {
      path: '/profile/:id/',
      name: 'ProfileView',
      component: ProfileView
    }, 
    {
      path: '/movies',
      name: 'MovieView',
      component: MovieView
    }, 
    {
      path: '/movies/:id/',
      name: 'MovieDetailView',
      component: MovieDetailView
    }, 
  ]
})



export default router