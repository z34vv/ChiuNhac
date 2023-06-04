from django.shortcuts import render
from django.views import View
from Home.models import Track
# Create your views here.


class ChartView(View):
    login_url = '/user/login'

    def get(self, request):
        Tracks = Track.object.order_by('-rate')
        chartNumber = range(1, 31)
        chartList = zip(chartNumber, Tracks)
        return render(request, 'charts.html',
                      {'Tracks': Tracks,
                       'chartList': chartList})
