from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r"groups", views.GroupViewSet, basename="categorygroup")
router.register(r"groups/(?P<group_id>\d+)/categories", views.CategoryViewSet, basename="category")
router.register(r"news", views.NewsViewSet, basename="news")


urlpatterns = [
    path("", include(router.urls)),
    path("feed/", views.NewsFeedView.as_view(), name="feed")
]

