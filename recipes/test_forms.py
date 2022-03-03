from django.test import TestCase
from .forms import RecipeForm


class TestRecipeForm(TestCase):
    '''
    Testing for Recipe Form
    '''

    # Tests to check required fields are not blank

    def test_recipe_title_is_required(self):
        '''
        Test to ensure title is present
        '''
        form = RecipeForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_recipe_description_is_required(self):
        '''
        Test to ensure description is present
        '''
        form = RecipeForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0], 'This field is required.'
            )

    def test_recipe_ingredients_is_required(self):
        '''
        Test to ensure ingredients is present
        '''
        form = RecipeForm({'ingredients': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(
            form.errors['ingredients'][0], 'This field is required.'
            )

    def test_recipe_method_is_required(self):
        '''
        Test to ensure method is present
        '''
        form = RecipeForm({'method': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('method', form.errors.keys())
        self.assertEqual(form.errors['method'][0], 'This field is required.')

    # Tests to check no profanity used

    def test_recipe_title_has_no_profanity(self):
        '''
        Test to insure title contains no profanity
        '''
        form = RecipeForm({'title': 'bitch'})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(
            form.errors['title'][0],
            'Please remove any profanity/swear words.'
            )

    def test_recipe_description_has_no_profanity(self):
        '''
        Test to insure description contains no profanity
        '''
        form = RecipeForm({'description': 'bitch'})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(
            form.errors['description'][0],
            'Please remove any profanity/swear words.'
            )

    def test_recipe_ingredients_has_no_profanity(self):
        '''
        Test to insure ingredients contains no profanity
        '''
        form = RecipeForm({'ingredients': 'bitch'})
        self.assertFalse(form.is_valid())
        self.assertIn('ingredients', form.errors.keys())
        self.assertEqual(
            form.errors['ingredients'][0],
            'Please remove any profanity/swear words.'
            )

    def test_recipe_method_has_no_profanity(self):
        '''
        Test to insure method contains no profanity
        '''
        form = RecipeForm({'method': 'bitch'})
        self.assertFalse(form.is_valid())
        self.assertIn('method', form.errors.keys())
        self.assertEqual(
            form.errors['method'][0],
            'Please remove any profanity/swear words.'
            )
