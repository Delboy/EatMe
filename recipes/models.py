from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.utils.text import slugify
from profanity.validators import validate_is_profane
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect


class Recipe(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, validators=[validate_is_profane])
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
    likes = models.ManyToManyField(User, related_name='recipe_likes', blank=True)

    class Meta:
        ordering = ['-published_on']

    def __str__(self):
        return self.title
    
    def number_of_likes(self):
        return self.likes.count()

    def save(self, *args, **kwargs):
        self.slug = '-'.join((slugify(self.author.id), slugify(self.title)))
        super(Recipe, self).save(*args, **kwargs)


class Comment(models.Model):
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name='comments'
        )
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField(validators=[validate_is_profane])
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f"Comment {self.body} by {self.name}"

    def get_absolute_url(self):
        return reverse('recipe_detail', args=[self.recipe.slug])
    
