from django.shortcuts import render
from django.views.generic import ListView
from .models import Recipe

# Create your views here.


class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipes.html"
    context_object_name = "recipes"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
