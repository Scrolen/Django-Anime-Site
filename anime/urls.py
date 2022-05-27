from django.urls import path

from .views import AnimeListView

urlpatterns = [
    path('', AnimeListView.as_view(), name='anime-home'),
    # path('genre/<genre>', AnimeHome.as_view(), name='anime-home'),

]