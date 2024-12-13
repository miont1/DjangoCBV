from django.urls import path
from recipes.views import RecipeList, RecipeCreate

urlpatterns = [
    path('', view=RecipeList.as_view(), name="recipe-list"),
    path('create-recipe/', view=RecipeCreate.as_view(), name="recipe-create"),
]