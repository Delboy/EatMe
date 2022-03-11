from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path(
        'your_recipes/', views.UsersRecipeList.as_view(), name='your_recipes'
        ),
    path('add_recipe/', views.AddRecipe.as_view(), name='add_recipe'),
    path(
        'edit_recipe/<int:pk>', views.EditRecipe.as_view(), name='edit_recipe'
        ),
    path(
        'edit_comment/<int:pk>',
        views.EditComment.as_view(), name='edit_comment'
        ),
    path(
        'delete_recipe/<int:recipe_id>',
        views.delete_recipe, name='delete_recipe'
        ),
    path(
        'delete_comment/<int:comment_id>',
        views.delete_comment, name='delete_comment'
        ),
    path(
        'favourite_recipes/',
        views.UsersFavRecipes.as_view(), name='favourite_recipes'),
    path('search_recipes/', views.search_recipes, name='search_recipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name="recipe_like")
]
