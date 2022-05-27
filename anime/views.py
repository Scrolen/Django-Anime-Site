from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView
from .models import Anime
# Create your views here.


class AnimeListView(ListView):
    model = Anime