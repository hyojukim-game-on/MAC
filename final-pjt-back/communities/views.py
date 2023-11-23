from django.shortcuts import redirect, render, get_list_or_404, get_object_or_404
from .serializers import *
from .models import *
from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes,permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])  
def article_list(request):
    # print('111111111111')
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # print('2222222222222')
        # print(request.data)
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            # print('333333333333333')
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','POST', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST','PUT','DELETE'])
def likes(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    print(request.user)
    if request.user in article.like_users.all():
        article.like_users.remove(request.user.id)
        is_liked = False
    else:
        article.like_users.add(request.user.id)
        is_liked = True
    data = {
        'is_liked': is_liked,
    }
    return Response(data=data, status=status.HTTP_200_OK)