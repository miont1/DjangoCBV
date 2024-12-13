import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView
from .models import Recipe
from .forms import CreateRecipe

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Create your views here.


class RecipeList(ListView):
    model = Recipe
    template_name = "recipes/recipes.html"
    context_object_name = "recipes"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["recipe_count"] = Recipe.objects.count()
        return context


class RecipeCreate(CreateView):
    model = Recipe
    template_name = "recipes/createRecipe.html"
    form_class = CreateRecipe
    success_url = reverse_lazy("recipe-list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            logger.info(f"Успішно додано рецепт: {self.object.title}")
            return JsonResponse(
                {"success": True, "message": "Recipe created successfully!"}
            )
        else:
            return JsonResponse({"success": False, "errors": form.errors})
