from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Album, Playlist, MusicStyle, Track, MusicVideo, LikeTrack, LikeMV, LikeAlbum, PlayingTrack
from User.models import CustomUser, Artist
from django.contrib.auth.mixins import LoginRequiredMixin
from User.views import UserView
# Create your views here.


class HomeView(LoginRequiredMixin, View):
    login_url = '/user/login'

    def get(self, request):
        user = request.user
        avatar = str(user.avatar)
        avatar_path = settings.MEDIA_ROOT + '/' + avatar
        avatar_url = settings.MEDIA_URL + avatar
        Tracks = Track.object.order_by('-created_at')
        MVs = MusicVideo.object.order_by('-created_at')
        Albums = Album.object.order_by('-created_at')
        Artists = Artist.object.order_by('-created_at')
        try:
            playingTrack = PlayingTrack.object.filter(user=user).order_by('-id').first()
        except PlayingTrack.DoesNotExist:
            playingTrack = Track.object.order_by('-created_at').first()
        return render(request, 'home.html',
                      {'avatar_path': avatar_path,
                       'avatar_url': avatar_url,
                       'Tracks': Tracks,
                       'MVs': MVs,
                       'Albums': Album,
                       'Artists': Artist,
                       'playingTrack': playingTrack})


def playing(request):
    user = request.user
    trackID = request.POST.get('trackID')
    try:
        track = Track.object.get(track_id=trackID)
        PlayingTrack.object.all().delete()
        playingTrack = PlayingTrack(track=track, user=user)
        playingTrack.track.rate += 1
        playingTrack.save()
    except Track.DoesNotExist:
        pass

    return redirect('playing_track/')


# def like(request):
#     if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
#         print("Clicked likeButton!")
#         user = request.user
#         user_like = Like.object.get(user=user)
#         objID = request.POST.get('objID')
#         try:
#             track = Track.object.get(track_id=objID)
#             likeTrack = '@' + objID
#             if likeTrack not in user_like.like_track:
#                 user_like.like_track = str(user_like.like_track) + likeTrack
#                 user_like.save()
#         except Track.DoesNotExist:
#             try:
#                 mv = MusicVideo.object.get(mv_id=objID)
#                 likeMV = '@' + objID
#                 if likeMV not in user_like.like_mv:
#                     user_like.like_mv = str(user_like.like_mv) + likeMV
#                     user_like.save()
#             except MusicVideo.DoesNotExist:
#                 album = Album.object.get(album_id=objID)
#                 likeAlbum = '@' + objID
#                 if likeAlbum not in user_like.like_album:
#                     user_like.like_album = str(user_like.like_album) + likeAlbum
#                     user_like.save()
#
#     return redirect('user/')

def likeTrack(request):
    user = request.user
    trackID = request.POST.get('objID')

    listTrackLiked = LikeTrack.object.filter(user=user)
    for item in listTrackLiked:
        if item.track.track_id == trackID:
            break
    else:
        track = Track.object.get(track_id=trackID)
        likeObj = LikeTrack(user=user, track=track)
        track.rate += 1
        likeObj.save()

    return redirect('user/')


def unlikeTrack(request):
    pass


def likeMV(request):
    user = request.user
    mvID = request.POST.get('objID')

    listMVLiked = LikeMV.object.filter(user=user)
    for item in listMVLiked:
        if item.mv.mv_id == mvID:
            break
    else:
        likeObj = LikeMV(user=user, track=Track.object.get(mv_id=mvID))
        likeObj.save()

    return redirect('user/')


def likeAlbum(request):
    user = request.user
    albumID = request.POST.get('objID')

    listAlbumLiked = LikeAlbum.object.filter(user=user)
    for item in listAlbumLiked:
        if item.album.album_id == albumID:
            break
    else:
        likeObj = LikeAlbum(user=user, album=Album.object.get(album_id=albumID))
        likeObj.save()

    return redirect('user/')
