# Generated by Django 4.2 on 2023-04-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='chapter_uploads/'),
        ),
    ]