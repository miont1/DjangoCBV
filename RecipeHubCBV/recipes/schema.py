import graphene
from graphene_django.types import DjangoObjectType
from users.models import Profile
from categories.models import Category


from .models import Recipe


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile

    username = graphene.String()

    def resolve_username(self, info):
        return self.user.username


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category

    name = graphene.String()

    def refolve_name(self, info):
        return self.name


class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = ("id", "title", "description", "ingredients", "created_at")

    owner = graphene.Field(ProfileType)

    def resolve_owner(self, info):
        return self.owner

    category = graphene.Field(CategoryType)

    def resolve_category(self, info):
        return self.category


class Query(graphene.ObjectType):
    all_recipes = graphene.List(RecipeType)

    def resolve_all_recipes(root, info):
        return Recipe.objects.all()


class CreateRecipe(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        ingredients = graphene.String(required=True)
        owner_id = graphene.Int(required=True)
        category = graphene.Int(required=False)

    recipe = graphene.Field(RecipeType)

    def mutate(self, info, title, description, ingredients, owner_id, category=None):
        category_instance = (
            Category.objects.filter(id=category).first() if category else None
        )
        recipe = Recipe.objects.create(
            title=title,
            description=description,
            ingredients=ingredients,
            owner_id=owner_id,
            category=category_instance,
        )
        return CreateRecipe(recipe=recipe)


class Mutation(graphene.ObjectType):
    create_recipe = CreateRecipe.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
