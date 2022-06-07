from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("anime-genre", kwargs={"slug": self.slug})
    ######################################################################################################
    # SAVE METHOD IS PLACE HOLDER FOR NOW....FIND A BETTER METHOD OR SEE IF THIS METHOD IS EFFICIENT
    #
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Anime(models.Model):
    name = models.CharField(max_length=150, unique=True)
    description = models.TextField()
    user_count = models.IntegerField()
    episodes = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    image = models.ImageField(default='anime_imgs/default.jpg', upload_to='anime_imgs')
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("anime-detail", kwargs={"slug": self.slug})

    ######################################################################################################
    # SAVE METHOD IS PLACE HOLDER FOR NOW....FIND A BETTER METHOD OR SEE IF THIS METHOD IS EFFICIENT
    #
    def save(self, *args, **kwargs): 
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


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

