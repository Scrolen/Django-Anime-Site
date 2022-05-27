from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Anime
# Create your views here.


class AnimeListView(ListView):
    model = Anime

class AnimeDeleteView(LoginRequiredMixin, DeleteView):
    model = Anime

    success_url = '/anime'


# def AnimeDeleteView(request, id):
#     anime = Anime.objects.get(id=id)
#     anime.delete()
#     return redirect('/anime/')
