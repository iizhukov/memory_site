from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'veterans', views.VeteranViewSet, basename='veteran')
router.register(r'birthday', views.BirthdayVeteransViewSet, basename='birthday')
router.register(r'notes', views.NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
]

