from rest_framework.viewsets import GenericViewSet, ModelViewSet

from projects.api.v1.serializers import AppSerializer
from projects.models import App


class AppViewSet(ModelViewSet):
    serializer_class = AppSerializer
    queryset = App.objects.all()

    def get_queryset(self, **kwargs):
        return super().get_queryset().filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
