"""Views"""

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.db.models import Count
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from .models import Recipe, Comment
from .forms import CommentForm, RecipeForm


class HomeView(View):
    """ Renders the home page"""
    def get(self, request):
        """What happens for a GET request"""
        recipes = Recipe.objects.filter(featured=True)
        top_recipes = Recipe.objects.annotate(
            like_count=Count('likes')).order_by('-like_count')
        context = {
            "recipes": recipes,
            "top_recipes": top_recipes
        }
        return render(request, 'index.html', context)


class RecipeList(View):
    """Renders all recipes"""
    def get(self, request):
        """What happens for a GET request"""
        recipes = Recipe.objects.all()
        paginator = Paginator(recipes, 6)  # Show 6 Recipes per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'recipes.html', {'page_obj': page_obj})


class RecipeDetail(View):
    """Renders recipe details"""
    def get(self, request, slug):
        """What happens for a GET request"""
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )

    def post(self, request, slug):
        """What happens for a POST request"""
        queryset = Recipe.objects.all()
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            messages.success(request, 'Comment added successfully')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            }
        )


class RecipeLike(View):
    """Likes/unlikes recipes"""
    def post(self, request, slug):
        """What happens for a POST request"""
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)
        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class UsersRecipeList(View):
    """Renders users recipes"""
    def get(self, request):
        """What happens for a GET request"""
        if request.user.is_authenticated:
            recipes = Recipe.objects.filter(author=request.user)
            paginator = Paginator(recipes, 6)  # Show 6 Recipes per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'your_recipes.html', {'page_obj': page_obj})
        else:
            return render(request, 'your_recipes.html')


class AddRecipe(SuccessMessageMixin, CreateView):
    """Adds Recipe"""
    model = Recipe
    form_class = RecipeForm
    template_name = 'add_recipe.html'
    success_message = 'Recipe Successfully Added'
    success_url = reverse_lazy('your_recipes')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditRecipe(SuccessMessageMixin, UpdateView):
    """Edits recipe"""
    model = Recipe
    template_name = 'edit_recipe.html'
    form_class = RecipeForm
    success_message = 'Recipe Successfully Updated'
    success_url = reverse_lazy('your_recipes')


def delete_recipe(request, recipe_id):
    """Deletes recipe"""
    recipe = get_object_or_404(Recipe, id=recipe_id)
    recipe.delete()
    messages.success(request, 'Recipe Deleted Successfully')
    return redirect(reverse('your_recipes'))


class EditComment(SuccessMessageMixin, UpdateView):
    """Edits comment"""
    model = Comment
    template_name = 'edit_comment.html'
    form_class = CommentForm
    success_message = 'Comment Successfully Updated'


def delete_comment(request, comment_id):
    """Deletes comment"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, 'Comment Deleted Successfully')
    return HttpResponseRedirect(reverse(
        'recipe_detail', args=[comment.recipe.slug]))


class UsersFavRecipes(View):
    """Renders users liked recipes"""
    def get(self, request):
        """What happens for a GET request"""
        if request.user.is_authenticated:
            recipes = Recipe.objects.filter(likes=request.user.id)
            paginator = Paginator(recipes, 6)  # Show 6 Recipes per page.
            page_number = request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            return render(request, 'favourite_recipes.html', {
                'page_obj': page_obj
                })
        else:
            return render(request, 'favourite_recipes.html')


def search_recipes(request):
    """Renders search results"""
    if request.method == "POST":
        searched = request.POST.get('searched')
        if searched.lower() == 'vegan':
            recipes = Recipe.objects.filter(vegan=True)
            return render(request, 'search_recipes.html', {
                'searched': searched, 'recipes': recipes
                })
        elif searched.lower() == 'vegetarian':
            recipes = Recipe.objects.filter(vegetarian=True)
            return render(request, 'search_recipes.html', {
                'searched': searched, 'recipes': recipes
                })
        else:
            recipes = Recipe.objects.filter(title__icontains=searched)
            return render(request, 'search_recipes.html', {
                'searched': searched, 'recipes': recipes
                })
    else:
        return render(request, 'search_recipes.html')
