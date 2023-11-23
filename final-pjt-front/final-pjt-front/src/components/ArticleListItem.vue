<template>
    <div class="py-3 my-2">
        <h5>No. {{ article.id }}</h5>
        <p>제목: {{ article.title }}</p>
        <!-- <p>내용: {{ article.content }}</p> -->
        <RouterLink :to="{ name: 'ArticleDetailView', params: {id: article.id}}">
            <v-btn 
            density="comfortable"
            >
                자세히보기
            </v-btn>
        </RouterLink>
        <v-icon 
        :icon="isLiked ? 'mdi mdi-thumb-up' : 'mdi mdi-thumb-up-outline'"
        @click="store.like(article.id)"
        ></v-icon>
        <v-divider></v-divider>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { RouterLink } from 'vue-router'
import { useAppStore } from '@/store/app'


const props = defineProps({
    article: Object,
    isLiked: Boolean,
})

const store = useAppStore()

</script>

<style scoped>

</style>