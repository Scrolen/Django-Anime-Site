# Generated by Django 4.0.4 on 2022-06-12 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0021_alter_anime_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='season',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='anime.season'),
        ),
    ]
