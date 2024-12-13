from django.urls import path

from .views import CategorieCreate, CategoryList


urlpatterns = [
    path("all/", view=CategoryList.as_view(), name="category-list"),
    path("create/", view=CategorieCreate.as_view(), name="category-create"),
    ]
