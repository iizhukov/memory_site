from rest_framework import serializers
from api.news import models


class CategoryGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryGroupModel
        fields = ['id', 'name', 'image', 'slug', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    group = CategoryGroupSerializer(read_only=True)

    class Meta:
        model = models.CategoryModel
        fields = ['id', 'group', 'name', 'description', 'slug', 'created_at']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.NewsModel
        fields = (
            'id', 'title', 'content', 'published_at', 
            'source', 'author', 'created_at', 'updated_at'
        )
        read_only_fields = ('author', 'created_at', 'updated_at')

