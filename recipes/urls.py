from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('recipes/', views.RecipeList.as_view(), name='recipes'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name="recipe_detail"),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name="recipe_like"),
]