# Generated by Django 4.2 on 2023-04-14 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0005_news_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='content',
        ),
    ]
