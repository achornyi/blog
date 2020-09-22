from .models import Article
from django.contrib.auth.models import User
from rest_framework import serializers


class AuthorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']


class ArticleDetailsSerializer(serializers.ModelSerializer):
    """Details of article"""
    author = AuthorNameSerializer()

    class Meta:
        model = Article
        fields = '__all__'


class ArticleSerializer(ArticleDetailsSerializer):
    """List of all articles"""

    class Meta:
        model = Article
        fields = ['title', 'last_update']


class ArticleCreateSerializer(ArticleDetailsSerializer):

    class Meta:
        model = Article
        fields = ['title', 'content', 'tags']

