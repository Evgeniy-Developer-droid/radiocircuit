# Generated by Django 4.2 on 2023-04-14 15:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0009_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
        migrations.CreateModel(
            name='PostContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_uploads_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='post_uploads_video/')),
                ('file', models.FileField(blank=True, null=True, upload_to='post_uploads_files/')),
                ('youtube', models.URLField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_content', to='content_app.post')),
            ],
        ),
        migrations.CreateModel(
            name='NewsContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='news_uploads_images/')),
                ('video', models.FileField(blank=True, null=True, upload_to='news_uploads_video/')),
                ('file', models.FileField(blank=True, null=True, upload_to='news_uploads_files/')),
                ('youtube', models.URLField(blank=True, null=True)),
                ('link', models.URLField(blank=True, null=True)),
                ('content', models.TextField(blank=True, default='', null=True)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_content', to='content_app.news')),
            ],
        ),
    ]
