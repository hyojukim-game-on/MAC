from django.db import models
from django.conf import settings
# Create your models here.
class Article(models.Model):
    # 외래키 클래스의 인스턴스 이름은, 참조하는 모델 클래스 이름의 단수형으로
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles')

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Comment(models.Model):
#     # 외래키 클래스의 인스턴스 이름은, 참조하는 모델 클래스 이름의 단수형으로
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)

#     content = models.TextField(max_length=300)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)