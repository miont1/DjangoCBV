from django.test import TestCase
from django.contrib.auth.models import User
from .models import Recipe, Profile, Category

# Create your tests here.


class RecipeModelTest(TestCase):

    def setUp(self):
        test_user = User.objects.create_user(username="test_user", password="password123")
        self.profile = Profile.objects.create(user=test_user)
        self.category = Category.objects.create(name="Dessert")

    def test_recipe_creation(self):
        recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test description",
            ingredients="Test ingredients",
            instructions="Test instructions",
            owner=self.profile,
            category=self.category,
        )

        self.assertEqual(recipe.title, "Test Recipe")
        self.assertEqual(recipe.category.name, "Dessert")
        self.assertEqual(recipe.owner.user.username, "test_user")

    def test_recipe_str_method(self):
        recipe = Recipe.objects.create(
            title="Test Recipe",
            description="Test description",
            ingredients="Test ingredients",
            instructions="Test instructions",
            owner=self.profile,
            category=self.category,
        )
        self.assertEqual(str(recipe), "Test Recipe")
