from django import forms
from django.forms import ModelForm

from categories.models import Category

from .models import Recipe


class CreateRecipe(ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreateRecipe, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({"class": "input"})
