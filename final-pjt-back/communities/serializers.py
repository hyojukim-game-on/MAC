from .models import Article
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault

# 게시글 목록
class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user','like_users',)


# 개별 게시글
class ArticleSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField(read_only=True)
    
    def get_user(self, obj):
        return obj.user.username
    
    class Meta:
        model = Article
        fields =  '__all__'
        read_only_fields = ('like_users',)


# class CommentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('article',)