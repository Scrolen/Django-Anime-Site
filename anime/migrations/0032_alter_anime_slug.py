# Generated by Django 4.0.4 on 2022-06-14 19:25

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0031_alter_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='slug',
            field=autoslug.fields.AutoSlugField(default='', editable=False, populate_from='name'),
        ),
    ]
