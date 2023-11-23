<template>
    <v-col class="v-col-auto">
        <v-card>
            <RouterLink :to="{ name: 'MovieDetailView', params: { id: currentMovie.id } }">
                <img :src="'https://image.tmdb.org/t/p/w200' + currentMovie.poster_path" alt="poster">
                <v-card-title>{{ currentMovie.title }}</v-card-title>
            </RouterLink>
        </v-card>
    </v-col>
</template>

<script setup>

const props = defineProps({
    currentMovie: Object
})


</script>

<style scoped>

</style>