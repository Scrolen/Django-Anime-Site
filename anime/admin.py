from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Anime, Genre, Review, WatchList

# Register your models here.

class AnimeAdmin(admin.ModelAdmin):
    filter_vertical = ('genres',)


class WatchListAdmin(admin.ModelAdmin):
    filter_horizontal = ('watched', 'wtwatch')

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Genre)
admin.site.register(WatchList, WatchListAdmin)
admin.site.register(Review)

