from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import *
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
import requests
import json
from bs4 import BeautifulSoup as bs
from django.db.models import Q, F, Case, When, Value, IntegerField
from django.utils import timezone
from rest_framework.pagination import PageNumberPagination





# 이 아래로 작성하시오.
API_KEY = 'a5401b53a16807a765df51132a428c09'
ACCESS_TOKEN = 'eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNTQwMWI1M2ExNjgwN2E3NjVkZjUxMTMyYTQyOGMwOSIsInN1YiI6IjY1M2IwOWE2YmMyY2IzMDE0ZDQ5OTJiMCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.oiXbBp3ak4MQnvbmhVhBOl6otIdSmNgkrpzTUOWKOPs'



@api_view(['GET'])
def movie_list(request):
    for n in range(1,1+50):
        url = f'https://api.themoviedb.org/3/movie/popular?api_key={API_KEY}&page={n}'
        response = requests.get(url)
        movies_data = response.json()['results']

        for movie_data in movies_data:
            # 영화 정보 저장
            movie = Movie.objects.get_or_create(
                title=movie_data['title'],
                defaults={
                    'genre_ids' : movie_data['genre_ids'],
                    'id': movie_data['id'],
                    'release_date': movie_data['release_date'],
                    'overview': movie_data['overview'],
                    'poster_path': movie_data['poster_path'],
                    'adult': movie_data['adult']
                }
            )
        # JSON 응답
        movies = Movie.objects.all().values()
    return JsonResponse({'movies': list(movies)})


@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['GET'])
def movie_search(request, search_id):
    '''
    search_id
    1 사람 수:1   관계:혼자       is_comfortable:True,   추천 장르 : 12                  , 결과 값 : 10+
    2 사람 수:1   관계:혼자       is_comfortable:False,  추천 장르 : 16                  , 결과 값 : 10+
    3 사람 수:2   관계:연인       is_comfortable:True,   추천 장르 : 10749,35,18         , 결과 값 : 10+
    4 사람 수:2   관계:연인       is_comfortable:False,  추천 장르 : 10749,53,28         , 결과 값 : 없음
    5 사람 수:2   관계:친구       is_comfortable:True,   추천 장르 : 53,28,80            , 결과 값 : 10+
    6 사람 수:2   관계:친구       is_comfortable:False,  추천 장르 : 35,28,16            , 결과 값 : 10+
    7 사람 수:2   관계:부모자식   is_comfortable:True,   추천 장르 : 10751,10402,35       , 결과 값 : 6
    8 사람 수:2   관계:부모자식   is_comfortable:False,  추천 장르 : 10751,18,36          , 결과 값 : 없음
    9 사람 수:2   관계:형제자매   is_comfortable:True,   추천 장르 : 16,14,53             , 결과 값 : 1
    10 사람 수:2  관계:형제자매   is_comfortable:False,  추천 장르 : 16,36,18             , 결과 값 : 없음
    11 사람 수:3+ 관계:친구들     is_comfortable:True,   추천 장르 : 12,36,99             , 결과 값 : 없음
    12 사람 수:3+ 관계:친구들     is_comfortable:False,  추천 장르 : 28,12,36             , 결과 값 : 4
    13 사람 수:3+ 관계:지인들     is_comfortable:True,   추천 장르 : 99,878,14            , 결과 값 : 없음
    14 사람 수:3+ 관계:지인들     is_comfortable:False,  추천 장르 : 28,12,16             , 결과 값 : 10+
    15 사람 수:3+ 관계:회사동료   is_comfortable:True,   추천 장르 : 27,14,53             , 결과 값 : 6
    16 사람 수:3+ 관계:회사동료   is_comfortable:False,  추천 장르 : 35,16,10402          , 결과 값 : 5
    17 사람 수:3+ 관계:가족들     is_comfortable:True,   추천 장르 : 10751,10402,35       , 결과 값 : 6
    18 사람 수:3+ 관계:가족들     is_comfortable:False,  추천 장르 : 10751,18,36          , 결과 값 : 없음
    '''
    search_conditions = {
    1: {'genres': ['12']},
    2: {'genres': ['16']},
    3: {'genres': ['10749', '35', '18']},
    4: {'genres': ['10749', '53', '28']},
    5: {'genres': ['53', '28', '80']},
    6: {'genres': ['35', '28', '16']},
    7: {'genres': ['10751', '10402', '35']},
    8: {'genres': ['10751', '18', '36']},
    9: {'genres': ['16', '14', '53']},
    10: {'genres': ['16', '36', '18']},
    11: {'genres': ['12', '36', '99']},
    12: {'genres': ['28', '12', '36']},
    13: {'genres': ['99', '878', '14']},
    14: {'genres': ['28', '12', '16']},
    15: {'genres': ['27', '14', '53']},
    16: {'genres': ['35', '16', '10402']},
    17: {'genres': ['10751', '10402', '35']},
    18: {'genres': ['10751', '18', '36']},
    }

    if search_id in search_conditions:
        
        genres = search_conditions[search_id]['genres']
        current_date = timezone.now().date()  # 현재 날짜 가져오기
        # 2000년 이후에서 현재 날짜까지의 영화
        movies = Movie.objects.filter(release_date__gte='2000-01-01', release_date__lte=current_date)
        
        q_objects = Q()
        for genre in genres:
            q_objects |= Q(genre_ids__contains=genre)

        movies = movies.filter(q_objects)
        movies = movies.order_by('-release_date') # 최신 영화가 먼저 나오게 정렬

        # 미래에 개봉하는 영화들 따로 분리
        future_movies = Movie.objects.filter(release_date__gt=current_date)


        # movies 를 pagination 을 적용하여 10개까지만 반환
        paginator = PageNumberPagination()
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(movies, request)


        # JSON으로 변환해서 반환
        serializer = MovieSerializer(result_page, many=True)
        future_movies_serializer = MovieSerializer(future_movies, many=True)
        
        # data 로 묶어서 제공
        data = {
            'current_movies': serializer.data,
            'future_movies': future_movies_serializer.data
            }
        
        return paginator.get_paginated_response(data)

    else:
        return Response({'error': 'Invalid Search ID'}, status=status.HTTP_400_BAD_REQUEST)