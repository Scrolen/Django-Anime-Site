from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DeleteView, DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.core.paginator import Paginator
from django.views.generic.list import MultipleObjectMixin

from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anime, Genre
# Create your views here.




class AnimeListView(ListView):
    paginate_by = 50
    model = Anime
    context_object_name = "anime_set"


class AnimeDetailView(DetailView):
    model = Anime
    context_object_name = "anime"
    


class AnimeDeleteView(LoginRequiredMixin, DeleteView):
    model = Anime

    success_url = '/anime'




class GenreDetailView(DetailView, MultipleObjectMixin):
    model = Genre
    paginate_by = 10

    def get_context_data(self, **kwargs):
        object_list = self.get_object().anime_set.all().order_by('name').values()
        context = super(GenreDetailView,self).get_context_data(object_list=object_list, **kwargs)
        return context


@login_required
def WatchListAdd(request, id):
    request.user.watchlist.watched.add(Anime.objects.get(id=id))
    return redirect(f'/anime/{Anime.objects.get(id=id).slug}')

def WatchListDelete(request, id):
    request.user.watchlist.watched.remove(Anime.objects.get(id=id))
    return redirect(f'/anime/{Anime.objects.get(id=id).slug}')

# def AnimeDeleteView(request, id):
#     anime = Anime.objects.get(id=id)
#     anime.delete()
#     return redirect('/anime/')
