from django.contrib import admin

from payments.models import Plan, Subscription


class PlanAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price", "created_at", "updated_at"]
    search_fields = ["name"]


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ["user", "plan", "project", "active", "created_at", "updated_at"]
    search_fields = ["plan__name", "user__name"]

    def project(self, obj):
        return obj.project


admin.site.register(Plan, PlanAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
