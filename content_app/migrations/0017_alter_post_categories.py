# Generated by Django 4.2 on 2023-04-22 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content_app', '0016_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='content_app.category'),
        ),
    ]
