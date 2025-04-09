from rest_framework import viewsets
from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
    OpenApiParameter,
)
from drf_spectacular.types import OpenApiTypes

from api.pagination import StandardPagination

from . import models
from . import serializers


class CategoryGroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.CategoryGroupModel.objects.all()
    serializer_class = serializers.CategoryGroupSerializer


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name='group_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.PATH,
            )
        ]
    )
)
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.CategorySerializer

    def get_queryset(self):
        group_id = self.kwargs.get('group_id')
        return models.CategoryModel.objects.filter(group_id=group_id)


@extend_schema_view(
    list=extend_schema(
        parameters=[
            OpenApiParameter(
                name='group_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            ),
            OpenApiParameter(
                name='category_id',
                type=OpenApiTypes.INT,
                location=OpenApiParameter.QUERY,
            )
        ],
    )
)
class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = serializers.NewsSerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        queryset = models.NewsModel.objects.filter()
        
        group_id = self.request.query_params.get('group_id')
        if group_id:
            queryset = queryset.filter(category__group_id=group_id)
        
        category_id = self.request.query_params.get('category_id')
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        
        return queryset.order_by('-created_at')
