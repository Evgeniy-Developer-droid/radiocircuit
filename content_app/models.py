import uuid
from django.db import models
from site_app.models import User
# from ckeditor.fields import RichTextField


class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="")
    slug = models.SlugField(unique=True, max_length=500)

    def __str__(self):
        return self.title


class News(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=255, default="")
    robots = models.CharField(max_length=255, null=True, default="index, follow", blank=True)
    keywords = models.TextField(max_length=500, null=True, default="", blank=True)
    slug = models.SlugField(unique=True, max_length=500)
    image = models.ImageField(upload_to="preview_image/")
    views = models.IntegerField(default=0)


class NewsContent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='news_uploads_images/', null=True, blank=True)
    video = models.FileField(upload_to='news_uploads_video/', null=True, blank=True)
    file = models.FileField(upload_to='news_uploads_files/', null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    content = models.TextField(default="", null=True, blank=True)
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name="news_content")


class Post(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="")
    description = models.TextField(max_length=255, default="")
    robots = models.CharField(max_length=255, null=True, default="index, follow", blank=True)
    keywords = models.TextField(max_length=500, null=True, default="", blank=True)
    slug = models.SlugField(unique=True, max_length=500)
    image = models.ImageField(upload_to="preview_image/")
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    categories = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)


class PostContent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    image = models.ImageField(upload_to='post_uploads_images/', null=True, blank=True)
    video = models.FileField(upload_to='post_uploads_video/', null=True, blank=True)
    file = models.FileField(upload_to='post_uploads_files/', null=True, blank=True)
    youtube = models.URLField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    content = models.TextField(default="", null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_content")