# Generated by Django 4.2 on 2023-04-13 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0004_remove_news_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
