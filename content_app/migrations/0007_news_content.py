# Generated by Django 4.2 on 2023-04-14 13:33

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0006_remove_news_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
        ),
    ]
