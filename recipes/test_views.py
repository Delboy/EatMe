"""Unit Tests for views"""

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Comment


class TestViews(TestCase):
    """
    Testing for Views
    """
    def setUp(self):
        test_user = User.objects.create_user(
            username='testuser', password='testpw'
            )
        self.recipe = Recipe.objects.create(title='Test', author=test_user)
        self.vegan_recipe = Recipe.objects.create(
            title='Vegan Recipe', vegan=True
            )
        self.vegetarian_recipe = Recipe.objects.create(
            title='Vegetarian Recipe', vegetarian=True
            )
        self.comment = Comment.objects.create(
            body='Test Comment', recipe=self.recipe
            )
        self.client.login(username='testuser', password='testpw')

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

    def test_get_your_recipes_page_if_user_logged_out(self):
        """
        Test to check your recipes page loads if user signed out
        """
        self.client.logout()
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

    def test_get_favourite_recipes_page_if_user_logged_out(self):
        """
        Test to check favourite recipes page loads if user signed out
        """
        self.client.logout()
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
        response = self.client.get(f'/{self.recipe.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipe_detail.html')

    def test_get_edit_recipes_page(self):
        """
        Test to ensure edit recipe page is displayed
        """
        response = self.client.get(f'/edit_recipe/{self.recipe.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_recipe.html')

    # Testing page functionality

    def test_can_add_recipe(self):
        """
        Testing recipes can be added to database
        """
        self.client.post('/add_recipe/', {
            'title': 'Test Title',
            'description': 'Test Desc',
            'ingredients': 'Test Ing',
            'method': 'Test method'
        })
        new_recipe = Recipe.objects.filter(title='Test Title')
        self.assertEqual(len(new_recipe), 1)

    def test_can_edit_recipe(self):
        """
        Testing editing a recipe
        """
        self.client.post(f'/edit_recipe/{self.recipe.id}', {
            'title': 'Edited Title',
            'description': 'Test Desc',
            'ingredients': 'Test Ing',
            'method': 'Test method'
        })
        edited_recipe = Recipe.objects.first().title
        self.assertEqual(edited_recipe, "Edited Title")

    def test_can_delete_recipe(self):
        """
        Testing Delete Recipes
        """
        response = self.client.get(f'/delete_recipe/{self.recipe.id}')
        self.assertRedirects(response, '/your_recipes/')
        existing_recipes = Recipe.objects.filter(id=self.recipe.id)
        self.assertEqual(len(existing_recipes), 0)

    def test_can_add_comment(self):
        """
        Testing comments can be added to database
        """
        self.client.post(f'/{self.recipe.slug}/', {'body': 'Test Comment'})
        self.assertEqual(Comment.objects.last().body, "Test Comment")

    def test_can_edit_comment(self):
        """
        Testing editing Comments
        """
        response = self.client.post(f'/edit_comment/{self.comment.id}', {
            'body': 'Edited Comment'
        })
        self.assertRedirects(response, f'/{self.comment.recipe.slug}/')
        edited_comment = Comment.objects.last().body
        self.assertEqual(edited_comment, "Edited Comment")

    def test_can_delete_comment(self):
        """
        Testing Deleting Comments
        """
        response = self.client.get(f'/delete_comment/{self.comment.id}')
        self.assertRedirects(response, f'/{self.comment.recipe.slug}/')
        existing_comments = Comment.objects.filter(id=self.comment.id)
        self.assertEqual(len(existing_comments), 0)

    def test_can_toggle_like_button(self):
        """
        Testing like button toggle
        """
        response = self.client.post(f'/like/{self.recipe.slug}')
        self.assertRedirects(response, f'/{self.recipe.slug}/')
        is_user_present = self.recipe.likes.filter(id=1).exists()
        self.assertTrue(is_user_present)
        response = self.client.post(f'/like/{self.recipe.slug}')
        is_user_present = self.recipe.likes.filter(id=1).exists()
        self.assertFalse(is_user_present)

    def test_liked_is_true_if_users_id_exists_in_recipes_liked_field(self):
        """
        Testing that the recipe shows as liked if the user has liked the recipe
        """
        response = self.client.post(f'/{self.recipe.slug}/')
        self.assertFalse(response.context['liked'])
        self.client.post(f'/like/{self.recipe.slug}')
        response = self.client.post(f'/{self.recipe.slug}/')
        self.assertTrue(response.context['liked'])
        user_present = self.recipe.likes.filter(id=1).exists()
        self.assertTrue(user_present)

    def test_using_search_bar_returns_searched_word_results(self):
        """
        Testing that the search bar returns results for the word searched
        """
        searched = 'Test'
        recipes = Recipe.objects.filter(title__icontains=searched)
        response = self.client.post('/search_recipes/', {
            'searched': searched,
            'recipes': recipes
        })
        self.assertEqual(response.context['searched'], 'Test')
        self.assertEqual(len(response.context['recipes']), 1)

    def test_searching_vegan_results_only_vegan_recipes(self):
        """
        Testing that searching the word vegan results in only vegan recipes
        """
        recipes = Recipe.objects.filter(vegan=True)
        response = self.client.post('/search_recipes/', {
            'searched': 'vegan',
            'recipes': recipes
        })
        self.assertEqual(response.context['searched'], 'vegan')
        self.assertEqual(len(response.context['recipes']), 1)

    def test_searching_vegetarian_results_only_vegetarian_recipes(
            self):
        """
        Testing that searching the word vegetarian
        results in only vegetarian recipes
        """
        recipes = Recipe.objects.filter(vegetarian=True)
        response = self.client.post('/search_recipes/', {
            'searched': 'vegetarian',
            'recipes': recipes
        })
        self.assertEqual(response.context['searched'], 'vegetarian')
        self.assertEqual(len(response.context['recipes']), 1)
