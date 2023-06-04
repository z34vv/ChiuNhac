from django.shortcuts import render
from Home.views import Album, Playlist, MusicStyle, Track, MusicVideo, CustomUser
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings
# Create your views here.


def searchView(request):
    query = request.GET.get('q')
    searchTracks = Track.object.filter(track_name__icontains=query) if query else []
    searchMVs = MusicVideo.object.filter(mv_name__icontains=query) if query else []
    searchAlbums = Album.object.filter(album_name__icontains=query) if query else []

    return render(request, 'search.html',
                  {'searchTracks': searchTracks,
                   'searchMVs': searchMVs,
                   'searchAlbums': searchAlbums,
                   'query': query})


def searchBar(request):
    return render(request, 'search_bar.html')
