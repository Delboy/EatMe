from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment
from django.urls import reverse
from django.test import Client


class TestViews(TestCase):
    """
    Testing for Views
    """

    # Testing page displays

    def test_get_home_page(self):
        """
        Test to ensure home page is displayed
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_all_recipes_page(self):
        """
        Test to ensure all recipes page is displayed
        """
        response = self.client.get('/recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes.html')

    def test_get_your_recipes_page(self):
        """
        Test to ensure your recipes page is displayed
        """
        response = self.client.get('/your_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'your_recipes.html')

    def test_get_add_recipes_page(self):
        """
        Test to ensure add recipes page is displayed
        """
        response = self.client.get('/add_recipe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'add_recipe.html')

    def test_get_favourite_recipes_page(self):
        """
        Test to ensure favourite recipes page is displayed
        """
        response = self.client.get('/favourite_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'favourite_recipes.html')

    def test_get_searched_recipes_page(self):
        """
        Test to ensure searched results page is displayed
        """
        response = self.client.get('/search_recipes/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search_recipes.html')

    def test_get_recipe_detail_page(self):
        """
        Test to ensure recipe detail page is displayed
        """
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        recipe = Recipe.objects.create(title='Test', author=test_user)
        response = self.client.get(f'/{recipe.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

    def test_get_edit_recipes_page(self):
        """
        Test to ensure edit recipe page is displayed
        """
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        recipe = Recipe.objects.create(title='Test', author=test_user)
        response = self.client.get(f'/edit_recipe/{recipe.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')

    # Testing page functionality

    def test_can_add_recipe(self):
        '''
        Testing recipes can be added to database
        '''
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        self.client.login(username='testuser', password='testpw')
        self.client.post('/add_recipe/', {
            'title': 'Test Title',
            'description': 'Test Desc',
            'ingredients': 'Test Ing',
            'method': 'Test method'
        })
        self.assertEqual(Recipe.objects.last().title, "Test Title")

    def test_can_delete_recipe(self):
        """
        Testing Delete Recipes
        """
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        recipe = Recipe.objects.create(title='Test', author=test_user)
        response = self.client.get(f'/delete_recipe/{recipe.id}')
        self.assertRedirects(response, '/your_recipes/')
        existing_recipes = Recipe.objects.filter(id=recipe.id)
        self.assertEqual(len(existing_recipes), 0)

    def test_can_add_comment(self):
        '''
        Testing comments can be added to database
        '''
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        recipe = Recipe.objects.create(title='Test', author=test_user)
        self.client.login(username='testuser', password='testpw')
        self.client.post(f'/{recipe.slug}/', {'body': 'Test Comment'})
        self.assertEqual(Comment.objects.last().body, "Test Comment")

    # def test_can_edit_comment(self):

    # def test_can_delete_comment(self):

    # def test_can_toggle_like(self):
