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