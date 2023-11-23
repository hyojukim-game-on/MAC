<template>
    <v-container class="py-8">
    <v-app-bar app color="deep-purple" dark>
        <v-app-bar-nav-icon @click="store.drawer = !store.drawer"> 
            <v-btn icon>
                <v-icon icon="mdi:mdi-menu"></v-icon>
            </v-btn>
        </v-app-bar-nav-icon>
        <v-toolbar-title>🎄 Movies in Any Case 🎄</v-toolbar-title>
        <v-spacer></v-spacer>
        <RouterLink :to="{ name: 'MovieSearchView'}">
            <v-btn icon>
                <v-icon icon="mdi mdi-movie-search-outline"></v-icon>
            </v-btn>
        </RouterLink>
    </v-app-bar>
    <v-navigation-drawer v-model="store.drawer">
        <v-list nav dense>
            <v-divider></v-divider>
            <v-list-item link title="홈으로" :to="{ name: 'HomeView' }"></v-list-item>
            <v-list-item link title="커뮤니티" :to="{ name: 'ArticleView' }"></v-list-item>
                
            
            <!-- isLogin === false 일 때 렌더링하기 -->
            <v-list-item link title="회원가입" :to="{ name: 'SignUpView' }" 
            v-if="!store.isLogin"></v-list-item>
            <v-list-item link title="로그인" :to="{ name: 'LogInView' }"
            v-if="!store.isLogin"></v-list-item>
                
            

            <!-- isLogin === true 일 때 렌더링하기 -->
                <v-list-item v-if="store.isLogin">
                    <div class="pa-2">
                    <v-btn block @click="logOut">
                    로그아웃
                    </v-btn>
                    </div>
                </v-list-item>
        
        
            </v-list>
    </v-navigation-drawer>
    </v-container>
</template>

<script setup>
import { useAppStore } from '@/store/app.js'
import { ref } from 'vue'
import { useRouter } from 'vue-router';
import { onMounted } from 'vue'


const store = useAppStore()
const router = useRouter()


const logOut = function () {
    // console.log('NavBar 에서 logOut 함수가 실행되었음')
    store.logOut()
}



</script>

<style scoped>

</style>