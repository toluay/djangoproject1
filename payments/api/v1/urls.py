from django.urls import path, include
from rest_framework.routers import DefaultRouter

from payments.api.v1.viewsets import PlanViewSet, SubscriptionViewSet

router = DefaultRouter()
router.register("plans", PlanViewSet)
router.register("subscriptions", SubscriptionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]