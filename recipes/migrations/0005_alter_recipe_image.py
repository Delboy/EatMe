# Generated by Django 3.2 on 2022-02-02 13:15

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
    ]
