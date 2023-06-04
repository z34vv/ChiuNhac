from django.db import models
from User.models import CustomUser, Artist
# Create your models here.


# class Like(models.Model):
#     like_id = models.BigAutoField(primary_key=True)
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
#     like_track = models.TextField(null=True, blank=True)
#     like_mv = models.TextField(null=True, blank=True)
#     like_album = models.TextField(null=True, blank=True)
#     object = models.Manager()


class Album(models.Model):
    album_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    like_user = models.TextField(null=True, blank=True)
    album_name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField()
    rate = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    object = models.Manager()

    def __str__(self):
        return self.album_name


class Playlist(models.Model):
    playlist_id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    playlist_name = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.ImageField()
    object = models.Manager()

    def __str__(self):
        return self.playlist_name


class MusicStyle(models.Model):
    style_id = models.BigAutoField(primary_key=True)
    style_name = models.CharField(max_length=100, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    object = models.Manager()

    def __str__(self):
        return self.style_name


class Track(models.Model):
    track_id = models.BigAutoField(primary_key=True)
    track_name = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.ImageField()
    duration = models.IntegerField(default=0)
    source_path = models.CharField(max_length=255, blank=False, null=False)
    style = models.ForeignKey(MusicStyle, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist, blank=True)
    like_user = models.TextField(null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    playlist = models.ManyToManyField(Playlist, blank=True)
    rate = models.BigIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    object = models.Manager()

    def __str__(self):
        return self.track_name


class MusicVideo(models.Model):
    mv_id = models.BigAutoField(primary_key=True)
    mv_name = models.CharField(max_length=100, blank=False, null=False)
    avatar = models.ImageField()
    duration = models.IntegerField(default=0)
    source_path = models.CharField(max_length=255, blank=False, null=False)
    style = models.ForeignKey(MusicStyle, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    artist = models.ManyToManyField(Artist, blank=True)
    like_user = models.TextField(null=True, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, blank=True)
    playlist = models.ManyToManyField(Playlist, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    rate = models.BigIntegerField(default=0)
    object = models.Manager()

    def __str__(self):
        return self.mv_name


class LikeTrack(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    track = models.ForeignKey(Track, null=True, blank=True, on_delete=models.CASCADE)
    object = models.Manager()


class LikeMV(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    mv = models.ForeignKey(MusicVideo, null=True, blank=True, on_delete=models.CASCADE)
    object = models.Manager()


class LikeAlbum(models.Model):
    user = models.ForeignKey(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, null=True, blank=True, on_delete=models.CASCADE)
    object = models.Manager()


class PlayingTrack(models.Model):
    track = models.OneToOneField(Track, null=True, blank=True, on_delete=models.CASCADE)
    user = models.OneToOneField(CustomUser, null=True, blank=True, on_delete=models.CASCADE)
    object = models.Manager()
