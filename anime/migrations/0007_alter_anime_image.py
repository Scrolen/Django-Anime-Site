# Generated by Django 4.0.4 on 2022-06-04 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0006_alter_anime_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.ImageField(default='/media/anime_imgs/default.jpg', upload_to='anime_imgs'),
        ),
    ]
