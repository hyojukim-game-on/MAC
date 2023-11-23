<template>
    <v-card class="py-8" elevation="8">
    <v-form>
        <v-container>
        <v-row>
            <v-col class="d-flex align-center justify-center">
            <h2>회원가입</h2>
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
            v-model.trim="password1">
            </v-text-field>
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="12">
            <div class="text-subtitle-1 text-medium-emphasis 
            d-flex align-center justify-space-between">비밀번호 확인</div>
            <v-text-field type="password" 
            placeholder="password confirmation" 
            variant="outlined" 
            v-model.trim="password2">
            </v-text-field>
            </v-col>
        </v-row>
        <v-row>
        <v-btn
        @click="signUp"
        block
        class="mb-8"
        color="deep-purple-lighten-2"
        size="large"
        >
        가입하기
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
const password1 = ref(null)
const password2 = ref(null)
const store = useAppStore()

// 입력된 데이터의 유효성 검사 진행하기
// 예시: 이메일 형식, 비밀번호 강도

const signUp = function () {
    const payload = {
        username : username.value,
        password1 : password1.value,
        password2 : password2.value
    }
    console.log('SignUpView통과')
    store.signUp(payload)
}

</script>

<style scoped>

</style>