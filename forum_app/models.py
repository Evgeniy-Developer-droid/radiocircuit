import uuid
from django.db import models

from site_app.models import User


class Chapter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    logo = models.ImageField(upload_to="chapter_uploads/", null=True, blank=True)
    title = models.CharField(max_length=255, default="", null=True)
    slug = models.SlugField(unique=True, max_length=500)

    def __str__(self):
        return self.title


class Topic(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255, default="", null=True)
    slug = models.SlugField(unique=True, max_length=500)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="topic_creator")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="topic_chapter")

    def __str__(self):
        return self.title
    

class Message(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    body = models.TextField(default="", null=True, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="message_creator")
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name="message_chapter")
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="message_topic")

    def __str__(self):
        return self.creator.username


class MessageFile(models.Model):
    FILE_TYPE = (
        ("image", "Image",),
        ("video", "Video",),
        ("document", "Document",),
        ("file", "File",),
    )
    created = models.DateTimeField(auto_now_add=True)
    token = models.UUIDField(default=uuid.uuid4, editable=False)
    file = models.FileField(upload_to='forum_uploads/', null=True, blank=True)
    file_type = models.CharField(max_length=255, choices=FILE_TYPE, default="file")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name="message_file_obj")
    