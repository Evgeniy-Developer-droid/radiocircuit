# Generated by Django 4.2 on 2023-04-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0002_news_views_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='body',
            field=models.TextField(default=''),
        ),
    ]
