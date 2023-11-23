<template>
    <div>
        <h2>바르고 고운말은 당신의 인성을 나타냅니다.😺</h2>
        <br>
        <br>
        <div v-if="article">
            <h5>No. {{ article.id }}</h5>
            <br>
            <p>{{ article.title }}</p>
            <h5>{{ article.user }}님</h5>
            <br>
            <div class="writtingBox">
                <h3>{{ article.content }}</h3>
            </div>
            <br>
                <h5>작성시간 : {{ article.created_at }}</h5>
                <h5>수정시간 : {{ article.updated_at }}</h5>
            <br>
            <v-btn variant="tonal" @click="deleteArticle">
                <h3>지우기</h3>
            </v-btn>
            <RouterLink :to="{ name: 'ArticleUpdateView', params: {id: article.id}}" >
                <v-btn variant="tonal">
                    <h3>고치기</h3>
                </v-btn>
            </RouterLink>
            <v-divider></v-divider>
        </div>
    </div>
</template>

<script setup>

import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAppStore } from '@/store/app'

const store = useAppStore()
const route = useRoute()
const article = ref('')
const comment = ref('')
const commentList = ref([])
const token = ref('')
const router = useRouter()

onMounted(()=>{
    axios({
        method: 'get',
        url: `${store.BASE_URL}/api/v1/articles/${route.params.id}`,
        headers: 
        {Authorization: `Token ${store.token}`},
    })
    .then((res) => {
        console.log(res.data)
        article.value = res.data
    })
    .catch((err)=>console.error(err))
})


const deleteArticle = function () {
    axios({
        method: 'delete',
        url: `${store.BASE_URL}/api/v1/articles/${route.params.id}`,
        headers: 
        {Authorization: `Token ${store.token}`},
    })
    .then((res)=>{
        console.log('삭제되었습니다')
        router.push({
            path: '/articles',
            name: 'ArticleView',
          })
    })
    .catch((err)=>{console.error(err)})
}

</script>

<style scoped>
.writtingBox {
    background: papayawhip;
}

</style>