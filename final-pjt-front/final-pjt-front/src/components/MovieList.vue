<template>
    <div class="py-3 my-2">
        <v-divider></v-divider>
    <v-sheet class="mx-auto">
        <v-slide-group center-active 
        show-arrows max-width="300">
            <v-slide-group-item 
            v-for="movie in store.movies"
            :key="movie.id">
                <RouterLink :to="{name:'MovieDetailView', params: {id: movie.id} }">
                    <v-card
                    class="ma-4">
                        <img :src="'https://image.tmdb.org/t/p/w500' + movie.poster_path" 
                        alt='poster'>
                        <v-card-title>{{ movie.title }}</v-card-title>
                    </v-card>
                </RouterLink>
            </v-slide-group-item>
        </v-slide-group>
    </v-sheet>
    </div>
</template>

<script setup>
    import MovieListItem from '@/components/MovieListItem.vue'
    import { useAppStore } from '@/store/app'

    const store = useAppStore()

</script>

<style scoped>

</style>