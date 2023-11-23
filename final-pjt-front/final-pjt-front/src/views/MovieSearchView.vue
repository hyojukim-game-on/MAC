<template>
    <div>
        <v-container>
            <v-card>
                <v-card-title>상황에 맞는 영화 찾기</v-card-title>
                <v-card-text>태그로 골라보기</v-card-text>
                <v-divider></v-divider>
                    <v-chip
                    v-for="(value, key) in searchConditionObj"
                    :key="key"
                    @click="search(key)"
                    :color="getColor(key)">{{ value }}</v-chip>
            </v-card>
        </v-container>
    </div>
</template>

<script setup>

import axios from 'axios'
import { ref } from 'vue'
import { useAppStore } from '@/store/app'
import { useRouter } from 'vue-router'
import { storeToRefs } from 'pinia';



const searchConditionObj = {
    '1': '혼자/긍정적',
    '2': '혼자/부정적',
    '3': '연인과/긍정적',
    '4': '연인과/부정적',
    '5': '친구와/긍정적',
    '6': '친구와/부정적',
    '7': '부모자식/긍정적',
    '8': '부모자식/부정적',
    '9': '형제자매/긍정적',
    '10': '형제자매/부정적',
    '11': '3명이상/친구들/긍정적',
    '12': '3명이상/친구들/부정적',
    '13': '3명이상/지인들/긍정적',
    '14': '3명이상/지인들/부정적',
    '15': '3명이상/회사동료/긍정적',
    '16': '3명이상/회사동료/부정적',
    '17': '3명이상/가족들/긍정적',
    '18': '3명이상/가족들/부정적'
}

const store = useAppStore()
const router = useRouter()


const search = function (key) {
    axios({
        method:'GET',
        url: `${store.BASE_URL}/api/v2/movies/search/${key}`,
        headers: {
            Authorization: `Token ${store.token}`
        }
    })
    .then((res)=>{
        store.searchData = res.data
        router.push({
            path: '/movies/search/results/',
            name: 'MovieSearchResultView',
        })
    })
    .catch((err)=>{console.error(err)})
}

const getColor = function (key) {
        // 색상을 조건에 따라 지정합니다.
    // 예: 가족 관련은 명도 3번, 긍정적은 primary 색상 등
        switch (key) {
        case '1': // 혼자/긍정적
        case '3': // 연인과/긍정적
        case '5': // 친구와/긍정적
        case '7': // 부모자식/긍정적
        case '9': // 형제자매/긍정적
        case '11': // 3명이상/친구들/긍정적
        case '13': // 3명이상/지인들/긍정적
        case '15': // 3명이상/회사동료/긍정적
        case '17': // 3명이상/가족들/긍정적
            return 'blue-accent-2';

        case '2': // 혼자/부정적
        case '4': // 연인과/부정적
        case '6': // 친구와/부정적
        case '8': // 부모자식/부정적
        case '10': // 형제자매/부정적
        case '12': // 3명이상/친구들/부정적
        case '14': // 3명이상/지인들/부정적
        case '16': // 3명이상/회사동료/부정적
        case '18': // 3명이상/가족들/부정적
            return 'green-accent-4';

        default:
            return 'grey'; // 기본 색상 (예외 처리)
        }
}

</script>

<style scoped>

</style>