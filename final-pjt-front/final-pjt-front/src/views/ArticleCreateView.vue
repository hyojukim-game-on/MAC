<template>
    <div>
    <v-card class="py-8" elevation="8">
    <v-form @submit.prevent="createArticle">
        <v-container>
        <v-row>
            <h2>새 글 쓰기</h2>   
        </v-row>
        <v-row>
            <v-col cols="12">
            <div class="text-subtitle-1 text-medium-emphasis">제목</div>
                <v-text-field 
                    placeholder="Fill in the title form" 
                    variant="outlined" 
                    v-model.trim="title">
                </v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
                <div class="text-subtitle-1 text-medium-emphasis 
                d-flex align-center justify-space-between">내용</div>
                <v-textarea 
                    auto-grow
                    rows="5"
                    row-height="10"
                    shaped
                    placeholder="Fill in the content form." 
                    variant="outlined" 
                    v-model.trim="content">
                </v-textarea>
            </v-col>
        </v-row>
        <v-row>
        <v-btn
        type="submit"
        block
        class="mb-8"
        color="deep-purple-lighten-2"
        size="large"
        >
        글쓰기
        </v-btn>
        </v-row>
        </v-container>
    </v-form>
    </v-card>
    </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAppStore } from '@/store/app'

const title = ref('')
const content = ref('')
const store = useAppStore()

const createArticle = function () {
    const newArticle = {
        title : title.value,
        content : content.value
    }
    console.log('ArticleCreateView 의 createArticle 함수가 작동함')
    store.createArticle(newArticle)
}


</script>

<style scoped>

</style>