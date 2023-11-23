<template>
    <div>
        <v-card>
            <img :src="'https://image.tmdb.org/t/p/w200' + this_movie.poster_path" 
                        alt='poster'>
            <v-card-title>{{ this_movie.title }}</v-card-title>
            <v-card-text>{{ this_movie.release_date }} 개봉</v-card-text>
            <v-card-text>줄거리</v-card-text>
            <v-card-text>{{ this_movie.overview }}</v-card-text>
            <v-card-text>장르 {{ genreNames }}</v-card-text>
        </v-card>
        <br><br><br>
        <RouterLink :to="{name: 'MovieView'}">
            <v-btn>영화 리스트로 돌아가기</v-btn>
        </RouterLink>
    </div>
</template>

<script setup>

import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, RouterLink } from 'vue-router'
import { useAppStore } from '@/store/app'

const store = useAppStore()
const route = useRoute()
const this_movie = ref('')
const genreObj = {
    '28':'Action',
    '12':'Adventure',
    '16':'Animation',
    '35':'Comedy',
    '80':'Crime',
    '99':'Documentary',
    '18':'Drama',
    '10751':'Family',
    '14':'Fantasy',
    '36':'History',
    '27':'Horror',
    '10402':'Music',
    '10749':'Romance',
    '878':'Science Fiction',
    '10770': 'TV Movie',
    '53': 'Thriller',
    '10752':'War',
    '37':'Western',
}

const genreNames = []
onMounted(()=>{
    axios({
        method: 'get',
        url: `${store.BASE_URL}/api/v2/movies/${route.params.id}/`,
    })
    .then((res) => {
        console.log(res.data)
        this_movie.value = res.data
        const genre_ids = JSON.parse(this_movie.value.genre_ids)
        genre_ids.forEach((id)=>{
            const genreName = genreObj[id]
            if (genreName) {
                genreNames.push(genreName)
            }
        })
    })
    .catch((err)=>console.error(err))
})


</script>

<style scoped>

</style>