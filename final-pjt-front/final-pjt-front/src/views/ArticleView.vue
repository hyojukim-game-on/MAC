<template>
    <div class="py-3 my-2">
        <h1>자유게시판</h1>
        <br>
        <br>
        <RouterLink :to="{ name: 'ArticleCreateView'}" >
            <v-btn variant="tonal">글쓰러가기</v-btn>
        </RouterLink>
        <br>
        <br>

        <ArticleList/>
        
        <RouterLink :to="{ name: 'ArticleCreateView'}" >
            <v-btn variant="tonal">글쓰러가기</v-btn>
        </RouterLink>
    </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue'
import { onMounted } from 'vue'
import { useAppStore } from '@/store/app'
import { RouterLink } from 'vue-router'

const store = useAppStore()

onMounted(()=>{
    store.getArticles()
})


</script>

<style scoped>

</style>