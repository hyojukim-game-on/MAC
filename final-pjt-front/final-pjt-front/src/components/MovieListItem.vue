<template>
    <div>
        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" alt='poster'>
        <p>{{ movie.title }}</p>
    </div>
</template>

<script setup>

import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useAppStore } from '@/store/app'

defineProps({
    movie: Object,
})

const store = useAppStore()
const route = useRoute()

</script>

<style scoped>

</style>