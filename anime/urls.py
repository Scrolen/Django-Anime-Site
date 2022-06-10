from django.urls import path

from .views import AnimeDeleteView, AnimeDetailView, WatchListAdd, WatchListDelete, GenreDetailView, AnimeListView


urlpatterns = [
    path('', AnimeListView.as_view(), name='anime-home'),
    path('<slug:slug>/', AnimeDetailView.as_view(), name='anime-detail'),
    path('genre/<slug:slug>', GenreDetailView.as_view(), name='anime-genre'),
    path('delete/<int:pk>', AnimeDeleteView.as_view(), name='anime-delete'),
    path('watchlist/add/<int:id>', WatchListAdd, name='watchlist-add'),
    path('watchlist/delete/<int:id>', WatchListDelete, name='watchlist-delete'),

]