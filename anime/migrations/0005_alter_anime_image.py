# Generated by Django 4.0.4 on 2022-06-04 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0004_rename_title_anime_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(default='anime_imgs/default.jpg', upload_to='anime_imgs'),
        ),
    ]
