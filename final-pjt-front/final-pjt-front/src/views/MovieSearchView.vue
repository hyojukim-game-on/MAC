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
                    :color="getColor(key)"
                    class="px-10 mx-3 my-2">{{ value }}</v-chip>
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
    '1': '혼자 영화에 몰입할 떄😎',
    '2': '혼자 영화로 시간 때울 때🤔',
    '3': '연인과 즐거운 시간을 보낼 때😈',
    '4': '연인과 싸웠지만 데이트는 하고 싶을 때💨',
    '5': '동네 친구와 만나서 영화 볼 때🙆‍♀️',
    '6': '친해진 지 얼마 안 된 사이와 영화 볼 때💁‍♀️',
    '7': '부모님과 영화 데이트🙌',
    '8': '어버이날 픽💜',
    '9': '호적메이트와의 영화 탐방💌',
    '10': '영화 보고 싶은데 같이 볼 사람이 호적메이트밖에 없을 때💫',
    '11': '찐친과 영화볼 때🧡',
    '12': '동창회에서 영화본다면✅',
    '13': '영화 모임을 처음 갈 때💛',
    '14': '처음 만난 사람들과 할 말 없을 때💗',
    '15': '회사 친구와 밖에서 만난다면🚲',
    '16': '부장님과 영화를 봐야만 한다면🚩',
    '17': '패밀리데이트👍',
    '18': '명절에 가족들과🌛'
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
            return 'deep-purple'
        case '3': 
            return 'green'
        case '5':
            return 'blue'
        case '7': 
            return 'red'
        case '9': 
            return 'pink'
        case '11': 
            return 'teal'
        case '13': 
            return 'cyan'
        case '15': 
            return 'purple'
        case '17': // 3명이상/가족들/긍정적
            return 'indigo';

        case '2': 
            return 'green-lighten-1'// 혼자/부정적
        case '4': 
            return 'light-green-accent-4' // 연인과/부정적
        case '6': 
            return 'light-green-darken-4'// 친구와/부정적
        case '8':
            return 'yellow-darken-4' // 부모자식/부정적
        case '10': 
            return 'amber' // 형제자매/부정적
        case '12': 
            return 'deep-orange-darken-1'// 3명이상/친구들/부정적
        case '14': 
            return 'brown-darken-4' // 3명이상/지인들/부정적
        case '16': 
            return 'blue-grey-darken-4'// 3명이상/회사동료/부정적
        case '18': // 3명이상/가족들/부정적
            return 'green-accent-4';

        default:
            return 'grey'; // 기본 색상 (예외 처리)
        }
}

</script>

<style scoped>

</style>