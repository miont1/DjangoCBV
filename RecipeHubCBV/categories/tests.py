from django.test import TestCase

from categories.models import Category

# Create your tests here.


class CategoryModelTest(TestCase):
        
        def setUp(self):
            self.name = Category.objects.create(name="Десерт")
            self.description = Category.objects.create(name="Нагорода за їжу")

        def test_recipe_creation(self):
            category = Category.objects.create(
                name="Десерт",
                description="Нагорода за їжу",
            )

            self.assertEqual(category.name, "Десерт")
            self.assertEqual(category.description, "Нагорода за їжу")

        def test_recipe_str_method(self):
            category = Category.objects.create(
                name="Десерт",
                description="Нагорода за їжу",
            )
            self.assertEqual(str(category), "Десерт")
