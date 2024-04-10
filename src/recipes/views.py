from django.shortcuts import render, redirect
from .models import Recipe
from django.views.generic import ListView, DetailView   
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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

