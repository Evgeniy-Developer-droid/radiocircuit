# Generated by Django 4.2 on 2023-04-14 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0008_remove_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=models.TextField(default=''),
        ),
    ]