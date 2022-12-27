from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class App(models.Model):
    WEB = "Web"
    MOBILE = "Mobile"

    TYPE_CHOICES = (
        (WEB, WEB),
        (MOBILE, MOBILE)
    )

    DJANGO = "Django"
    REACT_NATIVE = "React Native"

    FRAMEWORK_CHOICES = (
        (DJANGO, DJANGO),
        (REACT_NATIVE, REACT_NATIVE)
    )

    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    framework = models.CharField(max_length=30, choices=FRAMEWORK_CHOICES)
    domain_name = models.CharField(max_length=50, blank=True)
    screenshot = models.ImageField(blank=True)
    subscription = models.OneToOneField("payments.Subscription", related_name="project", on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, related_name="projects", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
