from django.urls import path
from .views import MovieListView, RatingListView

urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie-list'),
    path('ratings/', RatingListView.as_view(), name='rating-list'),
]