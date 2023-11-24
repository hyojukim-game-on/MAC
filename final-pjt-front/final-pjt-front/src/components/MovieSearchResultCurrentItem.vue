<template>
    <v-col class="v-col-auto">
      <v-card v-if="currentMovie.poster_path">
        <RouterLink :to="{ name: 'MovieDetailView', params: { id: currentMovie.id } }">
          <img :src="'https://image.tmdb.org/t/p/w500' + currentMovie.poster_path" alt="poster">
          <v-card-title class="truncate-text">{{ currentMovie.title }}</v-card-title>
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
.truncate-text {
  max-width: 200px; /* Adjust the max-width to your desired value */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}
</style>