<template>
<div>
    <MovieList/>
</div>

</template>

<script setup>
import MovieList from '@/components/MovieList.vue'

import { onMounted } from 'vue'
import { useAppStore } from '@/store/app'
import { RouterLink } from 'vue-router'

const store = useAppStore()

onMounted(()=>{
    store.getMovies()
})

</script>

<style scoped>

</style>