<template>
    <v-card class="py-8" elevation="8">
    <v-form>
        <v-container>
        <v-row>
            <v-col class="d-flex align-center justify-center">
            <h2>로그인</h2>
            </v-col>      
        </v-row>
        <v-row>
            <v-col cols="12">
            <div class="text-subtitle-1 text-medium-emphasis">이름</div>
            <v-text-field 
            placeholder="username" 
            variant="outlined" 
            v-model.trim="username"></v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
            <div class="text-subtitle-1 text-medium-emphasis 
            d-flex align-center justify-space-between">비밀번호</div>
            <v-text-field type="password" 
            placeholder="password" 
            variant="outlined" 
            v-model.trim="password">
            </v-text-field>
            </v-col>
        </v-row>
        <v-row>
        <v-btn
        @click="logIn"
        block
        class="mb-8"
        color="deep-purple-lighten-2"
        size="large"
        >
        LOGIN
        </v-btn>
        </v-row>
        </v-container>
    </v-form>
    </v-card>
</template>

<script setup>
import { ref } from 'vue'
import { useAppStore } from '@/store/app.js'

const username = ref(null)
const password = ref(null)
const store = useAppStore()

const logIn = function () {
    const payload = {
        username : username.value,
        password : password.value,
    }
    console.log('LogInView 에서 logIn 함수가 실행되었음')
    console.log(payload)
    store.logIn(payload)
}

// 입력된 데이터의 유효성 검사 진행하기
// 예시: 이메일 형식, 비밀번호 강도

</script>

<style scoped>

</style>