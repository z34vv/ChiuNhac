from django.shortcuts import render, HttpResponse, redirect
from django.views import View
from django.contrib.auth import login
from .forms import RegisterForm
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser
from Home.models import Album, Playlist, MusicStyle, Track, MusicVideo, LikeTrack, LikeAlbum, LikeMV, PlayingTrack
from django.conf import settings
# Create your views here.


class UserView(LoginRequiredMixin, View):
    login_url = '/user/login'

    def get(self, request):
        user = request.user
        user_avatar = str(user.avatar)
        avatar_path = settings.MEDIA_ROOT + '/' + user_avatar
        avatar_url = settings.MEDIA_URL + user_avatar

        # albumTempList = []
        # album_like_list_id = str(like_list.like_album).split('@')
        # if len(album_like_list_id) > 1:
        #     for i in range(1, len(album_like_list_id)):
        #         albumTempList.append(int(album_like_list_id[i]))
        # likeAlbums = Album.object.filter(album_id__in=albumTempList)
        likeAlbums = LikeAlbum.object.filter(user=user)

        playlists = Playlist.object.filter(user=user).order_by('-playlist_name')
        styles = MusicStyle.object.order_by('-created_at')

        # trackTempList = []
        # track_like_list_id = str(like_list.like_track).split('@')
        # if len(track_like_list_id) > 1:
        #     for i in range(1, len(track_like_list_id)):
        #         trackTempList.append(int(track_like_list_id[i]))
        # likeTracks = Track.object.filter(track_id__in=trackTempList)
        likeTracks = LikeTrack.object.filter(user=user)

        # mvTempList = []
        # mv_like_list_id = str(like_list.like_mv).split('@')
        # if len(mv_like_list_id) > 1:
        #     for i in range(1, len(mv_like_list_id)):
        #         mvTempList.append(int(mv_like_list_id[i]))
        # likeMVs = MusicVideo.object.filter(mv_id__in=mvTempList)
        likeMVs = LikeMV.object.filter(user=user)

        Artists = CustomUser.objects.filter(is_artist=1).order_by('follower')
        # try:
        #     playingTrack = PlayingTrack.object.filter(user=user).order_by('-id').first()
        # except PlayingTrack.DoesNotExist:
        #     playingTrack = Track.object.order_by('-created_at').first()
        return render(request, 'user.html',
                      {'avatar_path': avatar_path,
                       'avatar_url': avatar_url,
                       'likeAlbums': likeAlbums,
                       'Playlists': playlists,
                       'Styles': styles,
                       'likeTracks': likeTracks,
                       'likeMVs': likeMVs,
                       'Artists': Artists})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def repairName(request):
    user = request.user
    new_name = request.POST.get('new_name')
    img = request.POST.get('img')
    user.avatar = img
    user.username = new_name
    user.save()

    return redirect('/user/')


def createPlaylist(request):
    user = request.user
    name = request.POST.get('name')
    avatar = request.POST.get('img')
    playlist = Playlist(user=user, playlist_name=name, avatar=avatar)
    playlist.save()

    return redirect('/user/')


def createPlaylistView(request):
    return render(request, 'createPlaylistForm.html')
