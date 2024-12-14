import logging

from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from recipes.models import Recipe

from .forms import CreateCategory
from .models import Category

# Create your views here.

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)


class CategoryList(ListView):
    model = Category
    template_name = "categories/categories.html"
    context_object_name = "categories"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categorie_count"] = Category.objects.count()
        return context


class CategorieCreate(CreateView):
    model = Category
    template_name = "categories/categorieCreate.html"
    form_class = CreateCategory
    success_url = reverse_lazy("category-list")

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            self.object = form.save()
            logger.info(f"Успішно додано рецепт: {self.object.name}")
            return JsonResponse(
                {"success": True, "message": "Category created successfully!"}
            )
        else:
            return JsonResponse({"success": False, "errors": form.errors})
