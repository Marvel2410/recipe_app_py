from django.shortcuts import render, redirect
from .models import Recipe
from django.views.generic import ListView, DetailView   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import RecipeSearchForm
import pandas as pd



def home(request):
    return render(request, 'recipes/recipes_home.html')

@login_required
def recipe_details(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    return render(request, 'recipes/recipe_details.html', {'recipe': recipe})

@login_required
def recipes_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipes_list.html', {'recipes': recipes})

class RecipeListView(LoginRequiredMixin, ListView):     
    model = Recipe                                    
    template_name = 'recipes/recipes_list.html'             

class RecipeDetailView(LoginRequiredMixin, DetailView):    
    model = Recipe                                   
    template_name = 'recipes/recipe_details.html' 


def recipe_search(request):
    form = RecipeSearchForm(request.GET)
    recipes = []

    if form.is_valid():
        name = form.cleaned_data.get('name')
        ingredient = form.cleaned_data.get('ingredient')
        difficulty_level = form.cleaned_data.get('difficulty_level')
        category = form.cleaned_data.get('category')
        show_all = form.cleaned_data.get('show_all')

        # Only filter recipes if at least one search criterion is provided
        if name or ingredient or difficulty_level or category:
            recipes = Recipe.objects.all()
            if name:
                recipes = recipes.filter(name__icontains=name)
            if ingredient:
                recipes = recipes.filter(ingredients__icontains=ingredient)
            if difficulty_level:
                recipes = recipes.filter(difficulty_level=difficulty_level)
            if category:
                recipes = recipes.filter(category=category)
        elif show_all:
            recipes = Recipe.objects.all()

    context = {
        'form': form,
        'recipes': recipes
    }

    return render(request, 'recipes/recipe_search.html', context)
