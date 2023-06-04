from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from User.models import CustomUser
from Home.models import Album, Playlist, MusicStyle, Track, MusicVideo, PlayingTrack
from django.conf import settings
# Create your views here.


class PlayingTrackView(View, LoginRequiredMixin):
    login_url = '/user/login'

    def get(self, request):
        user = request.user
        user_avatar = str(user.avatar)
        avatar_path = settings.MEDIA_ROOT + '/' + user_avatar
        avatar_url = settings.MEDIA_URL + user_avatar

        playingTrack = PlayingTrack.object.filter(user=user).order_by('-id').first()
        return render(request, 'playingTrack.html', {'avatar_url': avatar_url,
                                                     'playingTrack': playingTrack})
