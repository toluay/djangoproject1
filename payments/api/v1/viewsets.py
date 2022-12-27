from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from payments.api.v1.serializers import PlanSerializer, SubscriptionSerializer
from payments.models import Plan, Subscription


class PlanViewSet(ModelViewSet):
    serializer_class = PlanSerializer
    queryset = Plan.objects.all()

    http_method_names = ["get"]


class SubscriptionViewSet(ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    http_method_names = ["get", "post", "patch", "put"]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def get_serializer_context(self):
        return {"request": self.request}

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
