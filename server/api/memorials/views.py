from rest_framework import viewsets

from api.pagination import StandartPagination

from . import models
from . import serializers


class MemorialViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.MemorialModelSerializer
    pagination_class = StandartPagination
    queryset = models.MemorialModel.objects.all()
