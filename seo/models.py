from django.db import models


class SeoPage(models.Model):
    page = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=500, null=True, default="", blank=True)
    description = models.TextField(max_length=500, null=True, default="", blank=True)
    robots = models.CharField(max_length=255, null=True, default="index, follow", blank=True)
    keywords = models.TextField(max_length=500, null=True, default="", blank=True)
    image = models.ImageField(upload_to="seo/", null=True, default="", blank=True)
