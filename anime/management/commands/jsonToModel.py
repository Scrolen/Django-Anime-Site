from ast import Import
import requests
import json
import os
import mimetypes
import urllib.parse

from django.core.management.base import BaseCommand, CommandError
from anime.models import Anime, Genre, Season

class Command(BaseCommand):
    help = 'Does some magical work'

    def handle(self, *args, **options):
        """ Do your work here """
        test = 'anime/management/commands/test.json'
        actual = 'anime/management/commands/anime-offline-database.json'


        # OPENS THE JSON FILE CONTAINING THE ANIME DATA FOR READING.
        with open(actual, encoding="utf8") as f:
            animeData = json.load(f)

        genreList = ['Action','Adventure','Abstract','Acting','Afterlife','Comedy','Dementia','Demons','Drama','Ecchi','Fantasy','Game','Harem',
        'Historical','Horror','Josei','Kids','Magic','Martial arts','Mecha','Military','Movie','Music','Mystery','ONA','OVA','Parody','Police',
        'Psychological','Romance','Samurai','School','Sci-fi','Seinen','Shounen','Slice of life','Space','Special','Sports','Supernatural', 'Super power',
        'Thriller','Vampire','Seinen','Gore','Manga','Revenge','Survival','Tragedy','Violence','War','Anti-hero','Crime','Kaiju','Thriller','Yandere','Tsundere',
        'High school','Swimming','Isekai','Dark fantasy','Shoujo']


        genreAvoid = ["anal","big boobs","bondage","boobjob","hentai","oral","softcore","big boobs",
        "hentai","incest","masturbation", "oral","softcore"]

        for anime in animeData['data']:

            safe = True
            title = anime['title']
            if not (Anime.objects.filter(name=title).exists()):
            
                ssnName = anime['animeSeason']['season']
                ssnYear = anime['animeSeason']['year']

                ssn,_ = Season.objects.get_or_create(season=ssnName,year=ssnYear, current="PAST")
                x = []
        

                for i in anime['tags']:
                    genreName = i.capitalize()
                    if i in genreAvoid:
                        safe = False
                    if genreName in genreList:
                        genre,_ = Genre.objects.get_or_create(name=genreName)
                        x.append(genre)

                if x and safe:

                    print(title)

                    animeObj = Anime(
                        name=title,
                        description='',
                        user_count=0,
                        episodes=anime['episodes'],
                        season = ssn,
                        status = anime['status'],
                        type = anime['type'],
                    )
                
                    animeObj.save()
                    animeObj.genres.set(x)

                    slug = animeObj.slug
                    downloadUrl = anime['picture']

                    path = urllib.parse.urlparse(downloadUrl).path
                    f_ext = os.path.splitext(path)[1]
                    
                    page = requests.get(downloadUrl)
                    # content_type = page.headers['content-type']
                    # f_ext = mimetypes.guess_extension(content_type)
                    # f_ext = os.path.splitext(downloadUrl)[-1]
                    
                    f_name = 'media/anime_imgs/{name}{ext}'.format(name=slug,ext=f_ext)
                    with open(f_name, 'wb') as f:
                        f.write(page.content)

                    animeObj.image = 'anime_imgs/{name}{ext}'.format(name=slug,ext=f_ext)
                    animeObj.save()


                    thumbnailUrl = anime['thumbnail']
                    path = urllib.parse.urlparse(thumbnailUrl).path
                    f_ext = os.path.splitext(path)[1]
                    page = requests.get(downloadUrl)

                    f_name = 'media/thumbnail/{name}-t{ext}'.format(name=slug,ext=f_ext)
                    with open(f_name, 'wb') as f:
                        f.write(page.content)




# IMAGE DOWNLOADING
# img_data = requests.get(anime['picture']).content
#     with open(anime['title'], 'wb') as handler:
#         handler.write(img_data)