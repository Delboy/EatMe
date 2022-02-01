from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'published_on', 'featured')
    search_fields = ['title', 'description', 'method', 'ingredients']
    prepopulated_fields = {'slug': ('author', 'title')}
    list_filter = ('published_on', 'author', 'featured', 'vegetarian', 'vegan')
    summernote_fields = ('ingredients', 'method')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'created_on')
    search_fields = ('name', 'email', 'body')
    list_filter = ('created_on',)
