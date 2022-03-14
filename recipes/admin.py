"""Options for admins page"""

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Recipe, Comment


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):
    """Admins recipe model features"""
    list_display = ('title', 'slug', 'published_on', 'featured')
    search_fields = ['title', 'description', 'method', 'ingredients']
    prepopulated_fields = {'slug': ('author', 'title')}
    list_filter = ('published_on', 'author', 'featured', 'vegetarian', 'vegan')
    summernote_fields = ('ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Admins comment model features"""
    list_display = ('name', 'body', 'recipe', 'created_on')
    search_fields = ('name', 'email', 'body')
    list_filter = ('created_on',)
