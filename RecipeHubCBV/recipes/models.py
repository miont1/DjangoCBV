from django.db import models

from categories.models import Category
from users.models import Profile

# Create your models here.


class Recipe(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    instructions = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipes",
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
