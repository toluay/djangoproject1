from rest_framework import serializers

from payments.models import Subscription, Plan
from projects.models import App


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = ["id", "name", "description", "price", "created_at", "updated_at"]


class SubscriptionSerializer(serializers.ModelSerializer):
    app = serializers.IntegerField(source="project.id")

    class Meta:
        model = Subscription
        fields = ["id", "user", "plan", "app", "active", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

    def validate_app(self, app_id):
        request = self.context.get("request")
        if not request:
            return app_id
        if not request.user.projects.filter(id=app_id).exists():
            raise serializers.ValidationError("App doesn't exist.")
        return app_id

    def create(self, validated_data):
        app_id = validated_data.get("project").get("id")
        app = App.objects.get(id=app_id)
        if app.subscription:
            raise serializers.ValidationError("Subscription already exists for project.")
        validated_data.pop("project")
        subscription = super().create(validated_data)
        app.subscription = subscription
        app.save()
        return subscription

    def update(self, instance, validated_data):
        app_id = validated_data.get("project", {}).get("id")
        if app_id and instance.project.id != app_id:
            raise serializers.ValidationError("Cannot change app of subscription.")
        validated_data.pop("project", None)
        return super().update(instance, validated_data)
