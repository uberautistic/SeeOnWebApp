from tkinter.font import names

from django.urls import path
from . import views
from .views import HomePageView, FilmPageView, CatalogView, CalibrationView

urlpatterns = [
    path('', HomePageView.as_view(), name='homepage'),
    path('movie/<int:pk>', FilmPageView.as_view(), name='movie_detail'),
    path('search-by-name/', views.search_film_by_name, name='search-by-name'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('search-country/', views.search_country, name='search-country'),
    path('search-directors/', views.search_directors, name='search-directors'),
    path('search-genres/', views.search_genres,name='search-genres'),
    path('toggle-movie-watchlist/', views.toggle_movie_watchlist, name='toggle-movie-watchlist'),
    path('toggle-preference/', views.toggle_preferencies, name='toggle-preference'),
    path('finish-calibration/', views.finish_calibration,name='finish_calibration'),
    path('cancel-calibration/',views.cancel_calibration, name='cancel-calibration'),
    path('calibration/', CalibrationView.as_view(), name='calibration'),
    path('refresh-recomendations/', views.refresh_recommendations, name='refresh_rec'),
    path('filter/', views.filter, name='filter')
]
