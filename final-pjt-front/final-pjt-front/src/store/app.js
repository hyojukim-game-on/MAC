// Utilities
import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter, useRoute } from 'vue-router'
axios.defaults.xsrfHeaderName = 'X-CSRFToken'
axios.defaults.xsrfCookieName = 'csrftoken'
axios.defaults.withCredentials = true


export const useAppStore = defineStore('app', () => {

    const movies = ref([])
    const articles = ref([])
    const BASE_URL = 'http://localhost:8000'
    const token = ref(null)
    const title = ref('')
    const content = ref('')
    const route = useRoute()
    const router = useRouter()
    const isLogin = computed(()=>{
      if (token.value === null) {
        return false
      } else {
        return true
      }
    })
    const isLikedObj = ref({})

    // 영화 가져오기
    const getMovies = function () {
      axios({
        method: 'get',
        url: `${BASE_URL}/api/v2/movies/`
      })
      .then((res)=>{
        // console.log(res.data)
        // console.log(res.data.movies)
        movies.value = res.data.movies
      })
      .catch((err)=>{console.error(err)})
    }


    // 게시글 가져오기
    const getArticles = function () {
      axios({
        method: 'get',
        url: `${BASE_URL}/api/v1/articles/`,
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
        .then(res => {
          // console.log(res.data)
          articles.value = res.data
        })
        
        .catch(err => console.log(err))
    }

    // 게시글 쓰기
    const createArticle = function (newArticle) {
      title.value = newArticle.title
      content.value = newArticle.content
      // console.log('app.js createArticle 들어옴')
      axios({
        method: 'post',
        url: `${BASE_URL}/api/v1/articles/`,
        data: {
          title: title.value,
          content: content.value
        },
        headers: {
          Authorization: `Token ${token.value}`
        }
      })
        .then((res)=>{
          router.push({
            path: '/articles',
            name: 'ArticleView',
          }
          )
        })
        .catch((err)=>{
          console.error(err)
        })
    }

    // 게시글 수정하기
    const updateArticle = function (newArticle) {
      title.value = newArticle.title
      content.value = newArticle.content
      // console.log('app.js updateArticle 들어옴')
      axios({
        method: 'put',
        url: `${BASE_URL}/api/v1/articles/${route.params.id}/`,
        data: {
          title: title.value,
          content: content.value
        },
        headers: {
          Authorization: `Token ${token.value}`,
        }
      })
        .then((res)=>{
          // router.router({
          //   path: '/articles',
          //   name: 'ArticleView',
          // })
        })
        .catch((err)=>{
          console.error(err)
        })
    }


    // 좋아요 action like 정의하기
    const like = function (articleId) {
      // 서버에 요청 보내기 (DB에 저장된 값과 동일하도록 하기)
      axios({
        method: 'get',
        url:`${BASE_URL}/api/v1/articles/${articleId}/likes/`,
        headers: {
          Authorization: `Token ${token.value}`
        }, 
      })
        .then((res)=>{
          // 잘 작동하는데 이 객체 방법의 문제가 있음
          // 다른 사용자가 로그인해서 좋아요를 아무것도 안 눌렀는데도
          // article 자체에 binding 했기 때문에 초기 값이
          // 다른 사용자가 좋아요를 했는지 아닌지로 나오고 있음..
          console.log(res.data.is_liked)
          // console.log(isLikedObj.value)
          isLikedObj.value[articleId] = res.data.is_liked
          // console.log(isLikedObj.value)
        })
        .catch((err)=>{console.error(err)})
    }



    // 회원가입
    const signUp = function (payload) {
      const username = payload.username
      const password1 = payload.password1
      const password2 = payload.password2
      // console.log('app.js signUp 들어옴')
      axios({
        method: 'post',
        url: `${BASE_URL}/accounts/signup/`,
        data: {
          username, password1, password2
        },
      })
        .then( (res) => {
          // console.log('회원가입이 완료되었습니다.')
          // 회원가입 화면에서.. '가입하기' 눌러서... 회원가입이 성공하면... 로그인 화면으로 RD 되게 하기.
          router.push({
            path: '/login',
            name: 'LogInView'
          }
          )
        })
        .catch( (err) => console.error(err))
    }


    // 로그인
    const logIn = function (payload) {
      const username = payload.username
      const password = payload.password
      // console.log('store 내부의 logIn 함수로 들어왔음')
      axios({
        method: 'post',
        url: `${BASE_URL}/accounts/login/`,
        data: {
          username, password
        },
      })
        .then((res)=>{
          token.value = res.data.key
          // console.log(username)
          // console.log('로그인 되셨어요 ^^')
          router.push({
            path: '/',
            name: 'HomeView'
          }
          )
          console.log(isLogin.value)
        })
        .catch((err)=>{
          console.error(`요청은 성공했고, 응답은 실패해서 ${err} 라고 돌아옴`)
        })
      }

    // 로그아웃
    const logOut = function () {
      // console.log('store 내부의 logOut 함수로 들어왔음')
      axios({
        method: 'post',
        url: `${BASE_URL}/accounts/logout/`
      })
        .then((res)=>{
          token.value = null
          // console.log(res)
          console.log('로그아웃 성공하셨어요 ^^')
          router.push({
            path: '/',
            name: 'HomeView'
          })
          console.log(isLogin.value)
        })
        .catch((err)=>{
          console.log(err)
        })
    }
    return { movies, getMovies, articles, 
      getArticles, BASE_URL, signUp, logIn, token, 
      logOut, createArticle, updateArticle, isLogin, like, isLikedObj}
    
}, {persist: true})