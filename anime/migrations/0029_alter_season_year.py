# Generated by Django 4.0.4 on 2022-06-14 17:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0028_alter_genre_name_alter_genre_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='season',
            name='year',
            field=models.PositiveIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(3000)]),
        ),
    ]
