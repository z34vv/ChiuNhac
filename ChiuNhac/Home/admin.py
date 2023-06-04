from django.contrib import admin
from .models import Album, Playlist, MusicStyle, Track, MusicVideo, LikeTrack, LikeMV, LikeAlbum, PlayingTrack
# Register your models here.


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['album_name',
                    'user',
                    'created_at']
    list_filter = ['album_name']


class PlaylistAdmin(admin.ModelAdmin):
    list_display = ['playlist_name']
    list_filter = ['playlist_name']


class MusicStyleAdmin(admin.ModelAdmin):
    list_display = ['style_name']
    list_filter = ['style_name']


class TrackAdmin(admin.ModelAdmin):
    list_display = ['track_name',
                    'duration',
                    'style',
                    'user',
                    'album',
                    'created_at']
    list_filter = ['track_name']


class MVAdmin(admin.ModelAdmin):
    list_display = ['mv_name',
                    'duration',
                    'style',
                    'user',
                    'album',
                    'created_at']
    list_filter = ['mv_name']


admin.site.register(Album, AlbumAdmin)
admin.site.register(Playlist, PlaylistAdmin)
admin.site.register(MusicStyle, MusicStyleAdmin)
admin.site.register(Track, TrackAdmin)
admin.site.register(MusicVideo, MVAdmin)
admin.site.register(LikeTrack)
admin.site.register(LikeMV)
admin.site.register(LikeAlbum)
admin.site.register(PlayingTrack)



