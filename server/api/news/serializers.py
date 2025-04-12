from rest_framework import serializers
from api.news import models


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GroupModel
        fields = ['id', 'name', 'image', 'description', 'slug', 'created_at']


class CategorySerializer(serializers.ModelSerializer):
    group = GroupSerializer(read_only=True)

    class Meta:
        depth = 1
        model = models.CategoryModel
        fields = ['id', 'group', 'name', 'description', 'slug', 'created_at']


class NewsSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        depth = 2
        model = models.NewsModel
        fields = (
            'id', 'category', 'title', 'content', 'published_at', 
            'source', 'author', 'created_at', 'updated_at', 'image',
        )
        read_only_fields = ('author', 'created_at', 'updated_at', 'published_at')
