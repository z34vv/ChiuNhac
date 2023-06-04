from django.urls import path
from .views import searchView, searchBar


urlpatterns = [
    path('search/', searchBar, name='search_bar'),
    path('search/results/', searchView, name='search_results')
]
