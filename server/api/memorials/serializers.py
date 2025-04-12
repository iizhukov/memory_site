from rest_framework import serializers
from api.memorials import models


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PhotoModel
        fields = '__all__'


class MemorialModelSerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = models.MemorialModel
        depth = 1
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
