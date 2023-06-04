from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Home.urls')),
    path('user/', include('User.urls')),
    path('chart/', include('Charts.urls')),
    path('search/', include('Search.urls')),
    path('playing_track/', include('PlayingTrack.urls'))
]
