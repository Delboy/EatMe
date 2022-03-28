"""Unit Tests for admin"""

from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.admin.sites import AdminSite
from .models import Recipe
from .admin import RecipeAdmin


class MockRequest(object):
    """setup mock request"""


request = MockRequest()


class TestAdmin(TestCase):
    """ Testing for admin  """
    def setUp(self):
        self.recipe_admin = RecipeAdmin(Recipe, AdminSite())
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        self.recipe1 = Recipe.objects.create(
            title='Test1',
            author=test_user,
            featured=False
            )
        self.recipe2 = Recipe.objects.create(
            title='Test2',
            author=test_user,
            featured=True)
        self.client.login(username='testuser', password='testpw')

    def test_make_featured_action(self):
        """
        Test to check the 'make featured' action updates featured field to true
        """
        queryset = Recipe.objects.filter(title='Test1')
        self.recipe_admin.make_featured(request, queryset)
        self.assertTrue(Recipe.objects.get(pk=1).featured)

    def test_activate_apps_should_activate_inactive_app2(self):
        """
        Test to check the 'unfeature' action updates featured field to false
        """
        queryset = Recipe.objects.filter(title='Test2')
        self.recipe_admin.unfeature(request, queryset)
        self.assertFalse(Recipe.objects.get(pk=1).featured)
