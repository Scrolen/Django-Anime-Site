# Generated by Django 4.0.4 on 2022-06-14 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0029_alter_season_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]