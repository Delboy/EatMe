"""Forms"""

from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Recipe


class CommentForm(forms.ModelForm):
    """Comments form"""
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields[
            'body'
            ].label = ""


class RecipeForm(forms.ModelForm):
    """Recipe Form"""
    class Meta:
        model = Recipe
        fields = (
            'title', 'description', 'ingredients', 'method',
            'vegetarian', 'vegan', 'image', 'image_url'
            )
        widgets = {
            'description': SummernoteWidget(),
            'ingredients': SummernoteWidget(),
            'method': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        self.fields[
            'vegetarian'
            ].label = "Is the recipe suitable for vegetarians?"
        self.fields['vegan'].label = "Is the recipe suitable for vegans?"
        self.fields['image'].label = "You can upload an image here"
        self.fields['image_url'].label = "OR input the image URL address here"
