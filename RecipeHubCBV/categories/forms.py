from django import forms
from django.forms import ModelForm

from .models import Category

class CreateCategory(ModelForm):
    class Meta:    
        model = Category
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(CreateCategory, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})