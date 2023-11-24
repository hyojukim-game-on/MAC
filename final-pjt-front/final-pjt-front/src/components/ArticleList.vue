<template>
    <div class="py-3 my-2 article-container">
        <v-divider></v-divider>
        <ArticleListItem
        v-for="article in store.articles"
        :key="article.id"
        :article="article"
        :is-liked="store.isLikedObj[article.id]"
        />
    </div>
</template>

<script setup>
    
    import ArticleListItem from '@/components/ArticleListItem.vue'
    import { useAppStore } from '@/store/app'

    const store = useAppStore()

</script>

<style scoped>
.article-container{
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
}
</style>