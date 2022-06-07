from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anime, Genre
# Create your views here.


class AnimeListView(ListView):
    model = Anime
    context_object_name = "anime_set"


class AnimeDetailView(DetailView):
    model = Anime
    context_object_name = "anime"
    


class AnimeDeleteView(LoginRequiredMixin, DeleteView):
    model = Anime

    success_url = '/anime'




class GenreDetailView(DetailView):
    model = Genre
    context_object_name = "genre"
    


@login_required
def WatchListAdd(request, id):
    request.user.watchlist.watched.add(Anime.objects.get(id=id))
    return redirect(f'/anime/{id}')

def WatchListDelete(request, id):
    request.user.watchlist.watched.remove(Anime.objects.get(id=id))
    return redirect(f'/anime/{id}')

# def AnimeDeleteView(request, id):
#     anime = Anime.objects.get(id=id)
#     anime.delete()
#     return redirect('/anime/')
