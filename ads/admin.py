from django.contrib import admin
from .models import Ad, AdImage, Category, Brand, Model


# 📸 изображения объявления
class AdImageInline(admin.TabularInline):
    model = AdImage
    extra = 3


# ✔️ действие: опубликовать
def publish_ads(modeladmin, request, queryset):
    queryset.update(is_published=True)

publish_ads.short_description = "✔️ Одобрить выбранные объявления"


# ❌ действие: скрыть
def unpublish_ads(modeladmin, request, queryset):
    queryset.update(is_published=False)

unpublish_ads.short_description = "❌ Снять с публикации"


# 📦 ОБЪЯВЛЕНИЯ
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "title",
        "author",
        "category",
        "brand",
        "model",
        "price",
        "city",
        "views",
        "favorites_count",
        "is_published",
        "created_at",
    )

    list_editable = (
        "is_published",
        "price",
    )

    list_filter = (
        "category",
        "brand",
        "is_published",
        "city",
        "created_at",
    )

    search_fields = (
        "title",
        "description",
        "author__username",
        "author__email",
    )

    ordering = ("-created_at",)

    actions = [
        publish_ads,
        unpublish_ads,
    ]

    inlines = [AdImageInline]

    list_per_page = 30

    readonly_fields = (
        "views",
        "favorites_count",
        "created_at",
    )


# 📂 КАТЕГОРИИ
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")


# 🏷 БРЕНДЫ
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category")
    list_filter = ("category",)


# 📦 МОДЕЛИ
@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand")
    list_filter = ("brand",)