# Generated by Django 4.0.5 on 2023-06-01 22:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_likealbum_likemv_liketrack_delete_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='created_at',
        ),
    ]