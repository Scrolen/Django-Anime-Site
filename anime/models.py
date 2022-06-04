from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name



class Anime(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    user_count = models.IntegerField()
    episodes = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    image = models.ImageField(default='anime_imgs/default.jpg', upload_to='anime_imgs')

    def __str__(self):
        return self.name


class Review(models.Model):
    review = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return '{id}-{anime}-{user}'.format(id = self.pk, anime = self.anime.title, user = self.user.username)

class WatchList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watched = models.ManyToManyField(Anime, related_name='watched', blank=True)
    wtwatch = models.ManyToManyField(Anime, related_name='wtwatch', blank=True)

    def __str__(self):
        return self.user.username

