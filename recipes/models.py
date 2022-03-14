"""Models"""

import datetime
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from profanity.validators import validate_is_profane


class Recipe(models.Model):
    """Model for Recipe"""
    title = models.CharField(
        max_length=200,
        null=False,
        blank=False,
        validators=[validate_is_profane]
        )
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes", null=True
        )
    published_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    description = models.TextField(validators=[validate_is_profane])
    ingredients = models.TextField(validators=[validate_is_profane])
    method = models.TextField(validators=[validate_is_profane])
    featured = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    image = CloudinaryField('image', default='placeholder')
    image_url = models.URLField(blank=True)
    likes = models.ManyToManyField(
        User,
        related_name='recipe_likes',
        blank=True
        )

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        """Returns number of likes"""
        return self.likes.count()

    def save(self, *args, **kwargs):
        now = datetime.datetime.now()
        d_truncated_date = datetime.date(now.year, now.month, now.day)
        d_truncated_time = datetime.time(now.hour, now.minute, now.second)
        self.slug = slugify(
            f'{self.author}-{self.title}-{d_truncated_date}-{d_truncated_time}'
            )
        super(Recipe, self).save(*args, **kwargs)


class Comment(models.Model):
    """Model for comments"""
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments'
        )
    name = models.CharField(max_length=80)
    body = models.TextField(validators=[validate_is_profane])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        """Sets absolute URL"""
        return reverse('recipe_detail', args=[self.recipe.slug])
