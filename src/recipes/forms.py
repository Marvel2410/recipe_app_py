from django import forms

DIFFICULTY_LEVEL_CHOICES = [
    ('', 'Any'),
    ('easy', 'Easy'),
    ('medium', 'Medium'),
    ('hard', 'Hard'),
]

CATEGORY_CHOICES = [
    ('', 'Any'),
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner'),
    ('snack', 'Snack'),
    ('dessert', 'Dessert'),
]

class RecipeSearchForm(forms.Form):
    name = forms.CharField(required=False, label='Recipe Name')
    ingredient = forms.CharField(required=False, label='Ingredient')
    difficulty_level = forms.ChoiceField(choices=DIFFICULTY_LEVEL_CHOICES, required=False, label='Difficulty Level')
    category = forms.ChoiceField(choices=CATEGORY_CHOICES, required=False, label='Category')
    
