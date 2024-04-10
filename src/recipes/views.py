from django.shortcuts import render, redirect
from .models import Recipe


def home(request):
    return render(request, 'recipes/recipes_home.html')

def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipes/recipe_details.html', {'recipe': recipe})

def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})



