# Generated by Django 4.0.4 on 2022-06-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0025_alter_anime_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]