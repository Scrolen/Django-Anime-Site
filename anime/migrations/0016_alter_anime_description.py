# Generated by Django 4.0.4 on 2022-06-12 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0015_alter_anime_description_alter_anime_episodes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.TextField(default='description'),
        ),
    ]
