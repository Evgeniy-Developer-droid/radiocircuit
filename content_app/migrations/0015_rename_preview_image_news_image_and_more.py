# Generated by Django 4.2 on 2023-04-20 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0014_news_keywords_news_robots_post_keywords_post_robots'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='preview_image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='preview_image',
            new_name='image',
        ),
    ]
