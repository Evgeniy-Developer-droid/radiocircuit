# Generated by Django 4.2 on 2023-04-13 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0003_news_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='body',
        ),
    ]