from django.contrib import admin

from categories.models import Category

from .models import Recipe

# Register your models here.

admin.site.site_header = "Адмінка сайту рецептів"
admin.site.site_title = "Адмінка рецептів"
admin.site.index_title = "Ласкаво просимо в адміністративну панель"


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):

    list_display = ("title", "owner", "category", "created_at")

    list_editable = ("category",)

    search_fields = (
        "id",
        "title",
    )

    list_filter = ("category", "created_at")

    ordering = ("-created_at",)

    fields = (
        "title",
        "description",
        "ingredients",
        "instructions",
        "owner",
        "category",
    )

    readonly_fields = ("created_at",)

    actions = ["set_default_category"]

    def set_default_category(self, request, queryset):
        default_category = Category.objects.get(name="Без категорії")
        queryset.update(category=default_category)
        self.message_user(request, "Категорію було оновлено для вибраних рецептів.")

    set_default_category.short_description = "Встановити категорію за замовчуванням"
