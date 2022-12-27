from django.urls import path, include
from rest_framework.routers import DefaultRouter

from projects.api.v1.viewsets import AppViewSet

router = DefaultRouter()

router.register("apps", AppViewSet)


urlpatterns = [
    path("", include(router.urls)),
]