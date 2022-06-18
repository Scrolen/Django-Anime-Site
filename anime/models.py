from email.policy import default
from pickle import TRUE
from tkinter import CASCADE
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image
from django.core.validators import MaxValueValidator
from numpy import minimum
from autoslug import AutoSlugField


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = AutoSlugField(populate_from='name', default="")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("anime-genre", kwargs={"slug": self.slug})
    ######################################################################################################
    # SAVE METHOD IS PLACE HOLDER FOR NOW....FIND A BETTER METHOD OR SEE IF THIS METHOD IS EFFICIENT
    #
    # def save(self, *args, **kwargs): 
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)


class Season(models.Model):

    SEASON_CHOICES = (
        ("SUMMER","Summer"),
        ("SPRING","Spring"),
        ("FALL","Fall"),
        ("WINTER","Winter"),
        ("UNDEFINED","Undefined"),
    )

    CURRENT_CHOICES = (
        ("CURRENT","Current"),
        ("PAST","Past"),
    )

    season = models.CharField(max_length=9, choices=SEASON_CHOICES, default="SUMMER")
    current = models.CharField(max_length=7, choices=CURRENT_CHOICES, default="PAST")
    year = models.PositiveIntegerField(validators=[MaxValueValidator(3000)],null=True)

    def __str__(self):
        return '{season} | {year}'.format(season=self.season, year=self.year)

class Anime(models.Model):

    STATUS_CHOICES = (
        ("ONGOING","Ongoing"),
        ("FINISHED","Finished"),
    )

    TYPE_CHOICES = (
        ("ONA", "ONA"),
        ("TV","TV"),
        ("SPECIAL","Special"),
        ("MOVIE","Movie"),
        ("OVA","OVA"),
    )

    name = models.CharField(max_length=150, unique=True)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=8, choices=STATUS_CHOICES, default="ONGOING")
    type = models.CharField(max_length=7, choices=TYPE_CHOICES, default="TV")
    season = models.ForeignKey(Season, on_delete=models.SET_NULL, default="", null=True)
    episodes = models.IntegerField(default= 0)
    genres = models.ManyToManyField(Genre)
    user_count = models.IntegerField(default=0)
    image = models.ImageField(default='anime_imgs/default.jpg', upload_to='anime_imgs')
    slug = AutoSlugField(populate_from='name', default="")


    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("anime-detail", kwargs={"slug": self.slug})

    ######################################################################################################
    # SAVE METHOD IS PLACE HOLDER FOR NOW....FIND A BETTER METHOD OR SEE IF THIS METHOD IS EFFICIENT
    #
    # def save(self, *args, **kwargs): 
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     return super().save(*args, **kwargs)







class Review(models.Model):
    review = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return '{id}-{anime}-{user}'.format(id = self.pk, anime = self.anime.name, user = self.user.username)






class WatchList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    watched = models.ManyToManyField(Anime, related_name='watched', blank=True)
    wtwatch = models.ManyToManyField(Anime, related_name='wtwatch', blank=True)

    def __str__(self):
        return self.user.username

