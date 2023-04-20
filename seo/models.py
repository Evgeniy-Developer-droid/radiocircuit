import uuid
from django.db import models


class Visitor(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=255, default="anonymus")
    ip = models.CharField(max_length=255, default="0.0.0.0")
    country = models.CharField(max_length=255, default="unknown")
    isp = models.CharField(max_length=255, default="unknown")


class SeoPage(models.Model):
    page = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=500, null=True, default="", blank=True)
    description = models.TextField(max_length=500, null=True, default="", blank=True)
    robots = models.CharField(max_length=255, null=True, default="index, follow", blank=True)
    keywords = models.TextField(max_length=500, null=True, default="", blank=True)
    image = models.ImageField(upload_to="seo/", null=True, default="", blank=True)
