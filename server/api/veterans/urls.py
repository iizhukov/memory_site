from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'veterans', views.VeteranViewSet, basename='veteran')
router.register(r'veterans/(?P<veteran_id>\d+)/notes', views.NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]

