# Generated by Django 4.0.5 on 2023-06-01 17:22

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('album_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('like_user', models.TextField(blank=True, null=True)),
                ('album_name', models.CharField(blank=True, max_length=255, null=True)),
                ('avatar', models.ImageField(upload_to='')),
                ('rate', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('like_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('like_track', models.TextField(blank=True, null=True)),
                ('like_mv', models.TextField(blank=True, null=True)),
                ('like_album', models.TextField(blank=True, null=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MusicStyle',
            fields=[
                ('style_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('style_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='MusicVideo',
            fields=[
                ('mv_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('mv_name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='')),
                ('duration', models.IntegerField(default=0)),
                ('source_path', models.CharField(max_length=255)),
                ('like_user', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('rate', models.BigIntegerField(default=0)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='PlayingTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlist_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('playlist_name', models.CharField(blank=True, max_length=255, null=True)),
                ('avatar', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('track_name', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='')),
                ('duration', models.IntegerField(default=0)),
                ('source_path', models.CharField(max_length=255)),
                ('like_user', models.TextField(blank=True, null=True)),
                ('rate', models.BigIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Home.album')),
            ],
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]