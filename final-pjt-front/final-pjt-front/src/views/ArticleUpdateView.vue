<template>
    <div>
    <v-card class="py-10" elevation="10">
    <v-form>
        <v-container>
        <v-row>
            <h2>글 수정하기</h2>   
        </v-row>
        <v-row>
            <v-col cols="12">
            <div class="text-subtitle-1 text-medium-emphasis">제목</div>
            <v-text-field 
            placeholder="Update your title"
            variant="outlined" 
            v-model.trim="title">
            </v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">

            <div class="text-subtitle-1 text-medium-emphasis 
            d-flex align-center justify-space-between">내용</div>

            <v-text-field 
            placeholder="Update your contents"
            variant="outlined" 
            v-model.trim="content">
            </v-text-field>

            </v-col>
        </v-row>

        <v-row>
        <v-btn
        type="submit"
        @click="updateArticle"
        block
        class="mb-8"
        color="deep-purple-lighten-2"
        size="large"
        >
        수정하기
        </v-btn>
        </v-row>
        </v-container>
    </v-form>
    </v-card>
    </div>
</template>

<script setup>


import axios from 'axios'
import { onMounted, ref } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useAppStore } from '@/store/app'

const article = ref('')
const title = ref('')
const content = ref('')
const store = useAppStore()
const route = useRoute()
const router = useRouter()
const token = ref('')

// 처음 수정하기 form 출력할 때 기존 글 데이터 불러와서 출력 미리 해주기
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


// 수정 버튼 누르면 수정 요청 보내기
const updateArticle = function () {
    const newArticle = {
        title : title.value,
        content : content.value,
    }
    console.log('ArticleUpdateView 의 updateArticle 통과')
    store.updateArticle(newArticle)

}


</script>

<style scoped>

</style>