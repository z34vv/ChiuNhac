from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ChartView.as_view(), name='chart')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
