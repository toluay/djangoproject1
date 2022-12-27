from django.contrib import admin

from projects.models import App


class AppAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "type", "framework", "domain_name", "user", "subscription", "screenshot", "created_at", "updated_at"]
    search_fields = ["name"]


admin.site.register(App, AppAdmin)
