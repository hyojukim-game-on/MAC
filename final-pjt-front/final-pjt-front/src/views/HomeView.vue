<template>
    <div>
        <div class="text-h1 text-center text-no-wrap">
            Movies in Any Case
        </div>
        <RouterLink :to="{name: 'MovieView'}">영화 리스트</RouterLink>
    </div>
</template>            

<script setup>

import { onMounted } from 'vue'
import { useAppStore } from '@/store/app'
import { RouterLink } from 'vue-router'

const store = useAppStore()

</script>

<style scoped>

</style>