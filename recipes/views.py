from django.shortcuts import render
from django.views import generic
from .models import Recipe


class HomeView(generic.ListView):
    def get(self, request):
        recipes = Recipe.objects.filter(featured=True)
        context = {
            "recipes": recipes
        }
        return render(request, 'index.html', context)