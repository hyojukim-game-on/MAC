from django.urls import path, include
from . import views

urlpatterns = [
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
]