import datetime
from rest_framework import viewsets
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from drf_spectacular.types import OpenApiTypes

from api.pagination import StandartPagination

from . import models
from . import serializers


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name='veteran_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            )
        ],
    )
)
class NoteViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NoteSerializer
    pagination_class = StandartPagination

    def get_queryset(self):
        queryset = models.NoteModel.objects.filter()
        
        veteran_id = self.request.query_params.get('veteran_id')
        if veteran_id:
            queryset = queryset.filter(veteran_id=veteran_id)
        
        return queryset.order_by('-created_at')


class VeteranViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.VeteranSerializer
    queryset = models.VeteranModel.objects.all()


class BirthdayVeteransViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.VeteranSerializer

    def get_queryset(self):
        today = datetime.date.today()
        return models.VeteranModel.objects.filter(birthday__day=today.day, birthday__month=today.month)
