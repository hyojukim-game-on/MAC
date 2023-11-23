<template>
  <v-app>
    <NavBar />
    <RouterView />
  </v-app>
</template>

<script setup>
  import NavBar from '@/components/NavBar.vue'
  import { RouterView } from 'vue-router'
</script>

<style scoped>
</style>