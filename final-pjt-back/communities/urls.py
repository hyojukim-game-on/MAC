from django.urls import path, include
from . import views

urlpatterns = [
    path('articles/', views.article_list, name='articles'),
    path('articles/<int:article_pk>/', views.article_detail, name='article_detail'),
    path('articles/<int:article_pk>/likes/', views.likes, name='likes'),
]
