from rest_framework.serializers import ModelSerializer

from projects.models import App


class AppSerializer(ModelSerializer):
    class Meta:
        model = App
        fields = ["id", "name", "description", "type", "framework", "domain_name", "screenshot", "subscription", "user", "created_at", "updated_at"]
        read_only_fields = ["id", "subscription", "user", "created_at", "updated_at"]
