from django.test import TestCase
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
