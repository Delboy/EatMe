"""Unit Tests for models"""

from freezegun import freeze_time
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Comment, Recipe


class TestModels(TestCase):
    """
    Testing for models
    """
    def test_recipe_model_str(self):
        """
        Testing that calling the string method returns correct string
        """
        recipe = Recipe.objects.create(title='Test Recipe')
        self.assertEqual(str(recipe), 'Test Recipe')

    def test_comment_model_str(self):
        """
        Testing that calling the string method returns correct string
        """
        recipe = Recipe.objects.create(title='Test Recipe')
        comment = Comment.objects.create(
            body='Test',
            recipe=recipe,
            name='Test_user'
            )
        self.assertEqual(str(comment), 'Comment Test by Test_user')

    def test_recipe_slug(self):
        """
        Testing the slug of a created recipe
        """
        with freeze_time("2022-1-1 12:30:30"):
            test_user = User.objects.create_user(
                username='testuser', password='testpw'
                )
            recipe = Recipe.objects.create(
                title='Test Recipe',
                author=test_user
                )
            self.assertEqual(
                recipe.slug, 'testuser-test-recipe-2022-01-01-123030'
                )
