from rest_framework import viewsets
from .models import NewsModel
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = NewsModel.objects.all().order_by('-published_at')
    serializer_class = NewsSerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

