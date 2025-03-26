from rest_framework import serializers
from api.news.models import NewsModel


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsModel
        fields = (
            'id', 'title', 'content', 'published_at', 
            'source', 'author', 'created_at', 'updated_at'
        )
        read_only_fields = ('author', 'created_at', 'updated_at')

