import uuid
from django.db import models
from content_app.fields import DynamicArrayField
from site_app.models import User
# Create your models here.

class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=255, default="")
    slug = models.SlugField(unique=True, max_length=500)
    preview_image = models.ImageField(upload_to="preview_image/")
    views = models.IntegerField(default=0)

    body = models.TextField(default="")


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=255, default="")
    slug = models.SlugField(unique=True, max_length=500)
    preview_image = models.ImageField(upload_to="preview_image/")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    views = models.IntegerField(default=0)