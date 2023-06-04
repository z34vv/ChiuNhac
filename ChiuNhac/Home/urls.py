from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('playing', views.playing, name='playing'),
    path('like_track', views.likeTrack, name='like_track'),
    path('like_mv', views.likeMV, name='like_mv'),
    path('like_album', views.likeAlbum, name='like_album'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
