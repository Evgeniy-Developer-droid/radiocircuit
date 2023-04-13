from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    key = models.UUIDField(default=uuid.uuid4, editable=False)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    rang = models.IntegerField(default=1)


class Token(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default="other", blank=True)
    