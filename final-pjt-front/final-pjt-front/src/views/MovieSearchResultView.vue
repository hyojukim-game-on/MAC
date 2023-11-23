<template>
    <div>
        <v-container>
        <h2>이런 영화 추천드려요!</h2>
        <v-row>
        <template 
        v-for="(currentMovie,index) in currentMovies"
        :key="currentMovie.id">
        
            <MovieSearchResultCurrentItem :currentMovie="currentMovie"/>
        
        </template>
        </v-row>
    </v-container>
    </div>
</template>

<script setup>
import MovieSearchResultCurrentItem from '@/components/MovieSearchResultCurrentItem.vue'
import { useAppStore } from '@/store/app'
import { ref } from 'vue'

const store = useAppStore()


const currentMovies = ref([])
// const futureMovies = ref('')
currentMovies.value = store.searchData.results.current_movies
console.log(store.searchData.results)

</script>

<style scoped>

</style>