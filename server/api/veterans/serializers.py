from rest_framework import serializers
from api.veterans import models


class VeteranSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VeteranModel
        fields = '__all__'


class NoteSerializer(serializers.ModelSerializer):
    veteran = VeteranSerializer(read_only=True)

    class Meta:
        model = models.NoteModel
        fields = '__all__'
