from django.urls import path

from .views import AnimeDeleteView, AnimeListView
from anime import views

urlpatterns = [
    path('', AnimeListView.as_view(), name='anime-home'),
    # path('genre/<genre>', AnimeHome.as_view(), name='anime-home'),
    path('delete/<int:pk>', AnimeDeleteView.as_view(), name='anime-delete'),
    

]