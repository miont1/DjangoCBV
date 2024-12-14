from django.urls import path
from recipes.views import RecipeList, RecipeCreate, RecipeView

urlpatterns = [
    path('', view=RecipeList.as_view(), name="recipe-list"),
    path('<int:pk>/', view=RecipeView.as_view(), name="recipe-view"),
    path('create-recipe/', view=RecipeCreate.as_view(), name="recipe-create"),
]