from django.test import TestCase
from .models import Recipe, Comment


class TestModels(TestCase):
    
    def test_featured_defaults_to_false(self):
        recipe = Recipe.objects.create(title='Test')
        self.assertFalse(recipe.featured)
