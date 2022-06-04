from django.urls import path

from .views import AnimeDeleteView, AnimeListView, AnimeDetailView, WatchListAdd, WatchListDelete
from anime import views

urlpatterns = [
    path('', AnimeListView.as_view(), name='anime-home'),
    path('<int:pk>/', AnimeDetailView.as_view(), name='anime-detail'),
    # path('genre/<genre>', AnimeHome.as_view(), name='anime-home'),
    path('delete/<int:pk>', AnimeDeleteView.as_view(), name='anime-delete'),
    path('watchlist/add/<int:id>', WatchListAdd, name='watchlist-add'),
    path('watchlist/delete/<int:id>', WatchListDelete, name='watchlist-delete'),

    

]