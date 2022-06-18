from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Anime, Genre, Review, Season, WatchList

# Register your models here.

class AnimeAdmin(admin.ModelAdmin):
    filter_vertical = ('genres',)
    list_display = ("name",)


class WatchListAdmin(admin.ModelAdmin):
    filter_horizontal = ('watched', 'wtwatch')

class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)

admin.site.register(Anime, AnimeAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(WatchList, WatchListAdmin)
admin.site.register(Review)
admin.site.register(Season)

