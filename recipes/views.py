from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Recipe


class HomeView(generic.ListView):
    def get(self, request):
        recipes = Recipe.objects.filter(featured=True)
        context = {
            "recipes": recipes
        }
        return render(request, 'index.html', context)


class RecipeList(generic.ListView):
    model = Recipe
    template_name = "recipes.html"
    paginate_by = 6


class RecipeDetail(View):

    def get(self, request, slug, *args, **kwargs):
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
            }
        )