# Generated by Django 4.0.4 on 2022-06-06 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0010_alter_watchlist_watched_alter_watchlist_wtwatch'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
