from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.db.models import Count

from .models import (
    Ad, AdImage, Category, Brand, Model,
    Profile, Favorite, Review, Chat, Message, Payment
)


# ─── ACTIONS ────────────────────────────────────────────────────────────────

def publish_ads(modeladmin, request, queryset):
    queryset.update(is_published=True)
publish_ads.short_description = "✔ Одобрить выбранные"

def unpublish_ads(modeladmin, request, queryset):
    queryset.update(is_published=False)
unpublish_ads.short_description = "✖ Снять с публикации"

def pin_ads(modeladmin, request, queryset):
    queryset.update(is_pinned=True)
pin_ads.short_description = "📌 Закрепить наверху"

def unpin_ads(modeladmin, request, queryset):
    queryset.update(is_pinned=False)
unpin_ads.short_description = "❌ Открепить"


# ─── INLINE ─────────────────────────────────────────────────────────────────

class AdImageInline(admin.TabularInline):
    model = AdImage
    extra = 0
    max_num = 10
    fields = ("image", "preview")
    readonly_fields = ("preview",)

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="height:60px;border-radius:6px;">', obj.image.url)
        return "—"
    preview.short_description = "Превью"


# ─── ОБЪЯВЛЕНИЯ ─────────────────────────────────────────────────────────────

@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):

    list_display = (
        "id", "pin_badge", "thumbnail", "title", "author_link",
        "category", "brand", "price_fmt",
        "city", "views", "fav", "status_badge",
        "created_at",
    )
    list_display_links = ("id", "title")
    list_filter = ("is_pinned", "is_published", "category", "brand", "city", "created_at")
    search_fields = ("title", "description", "author__username", "author__email", "city")
    ordering = ("-is_pinned", "-created_at",)
    actions = [pin_ads, unpin_ads, publish_ads, unpublish_ads]
    inlines = [AdImageInline]
    list_per_page = 30
    date_hierarchy = "created_at"
    readonly_fields = ("views", "favorites_count", "created_at", "expires_at")
    raw_id_fields = ("author", "category", "brand", "model")

    fieldsets = (
        ("Основное", {
            "fields": ("title", "description", "price", "city", "author", "is_published")
        }),
        ("Категория", {
            "fields": ("category", "brand", "model")
        }),
        ("Авто", {
            "classes": ("collapse",),
            "fields": ("year", "mileage", "transmission", "engine", "drive", "power", "wheel", "color")
        }),
        ("Телефон", {
            "classes": ("collapse",),
            "fields": ("memory",)
        }),
        ("Продвижение", {
            "classes": ("collapse",),
            "fields": ("is_pinned", "is_promoted", "promotion_level", "promoted_at", "promoted_until")
        }),
        ("Статистика", {
            "fields": ("views", "favorites_count", "created_at", "expires_at")
        }),
    )

    def pin_badge(self, obj):
        if obj.is_pinned:
            return format_html('<span title="Закреплено" style="font-size:16px;">📌</span>')
        return ""
    pin_badge.short_description = "📌"
    pin_badge.admin_order_field = "is_pinned"

    def thumbnail(self, obj):
        img = obj.images.first()
        if img and img.image:
            return format_html('<img src="{}" style="height:40px;width:52px;object-fit:cover;border-radius:5px;">', img.image.url)
        if obj.image:
            return format_html('<img src="{}" style="height:40px;width:52px;object-fit:cover;border-radius:5px;">', obj.image.url)
        return "—"
    thumbnail.short_description = ""

    def author_link(self, obj):
        return format_html('<a href="/admin/auth/user/{}/change/">{}</a>', obj.author.id, obj.author.username)
    author_link.short_description = "Автор"

    def price_fmt(self, obj):
        return f"{obj.price:,} ₸".replace(",", " ")
    price_fmt.short_description = "Цена"
    price_fmt.admin_order_field = "price"

    def fav(self, obj):
        return obj.favorites_count
    fav.short_description = "❤"
    fav.admin_order_field = "favorites_count"

    def status_badge(self, obj):
        if obj.is_published:
            return format_html('<span style="background:#1a4a1a;color:#81c784;padding:3px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;">✔ Опубликовано</span>')
        return format_html('<span style="background:#4a1a1a;color:#ef9a9a;padding:3px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;">⏳ Модерация</span>')
    status_badge.short_description = "Статус"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("author", "category", "brand").prefetch_related("images")


# ─── КАТЕГОРИИ ──────────────────────────────────────────────────────────────

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brands_count")
    search_fields = ("name",)

    def brands_count(self, obj):
        return obj.brands.count()
    brands_count.short_description = "Брендов"

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(_count=Count("brands"))


# ─── БРЕНДЫ ─────────────────────────────────────────────────────────────────

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "models_count")
    list_filter = ("category",)
    search_fields = ("name", "category__name")

    def models_count(self, obj):
        return obj.models.count()
    models_count.short_description = "Моделей"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("category").annotate(_count=Count("models"))


# ─── МОДЕЛИ ─────────────────────────────────────────────────────────────────

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "brand", "category_name")
    list_filter = ("brand__category", "brand")
    search_fields = ("name", "brand__name")

    def category_name(self, obj):
        return obj.brand.category.name
    category_name.short_description = "Категория"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("brand__category")


# ─── ПРОФИЛИ ────────────────────────────────────────────────────────────────

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "phone", "telegram", "avatar_thumb")
    search_fields = ("user__username", "user__email", "phone")
    raw_id_fields = ("user",)

    def avatar_thumb(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" style="height:36px;width:36px;border-radius:50%;object-fit:cover;">', obj.avatar.url)
        return "—"
    avatar_thumb.short_description = "Фото"


# ─── ОТЗЫВЫ ─────────────────────────────────────────────────────────────────

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "target", "stars", "short_text", "created_at")
    list_filter = ("rating", "created_at")
    search_fields = ("author__username", "target__username", "text")
    ordering = ("-created_at",)
    raw_id_fields = ("author", "target")

    def stars(self, obj):
        return "★" * obj.rating + "☆" * (5 - obj.rating)
    stars.short_description = "Оценка"

    def short_text(self, obj):
        return obj.text[:60] + "…" if len(obj.text) > 60 else obj.text
    short_text.short_description = "Текст"


# ─── ЧАТЫ ───────────────────────────────────────────────────────────────────

@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = ("id", "ad_link", "buyer", "seller", "messages_count", "created_at")
    search_fields = ("buyer__username", "seller__username", "ad__title")
    ordering = ("-created_at",)
    raw_id_fields = ("ad", "buyer", "seller")

    def ad_link(self, obj):
        return format_html('<a href="/admin/ads/ad/{}/change/">{}</a>', obj.ad.id, obj.ad.title[:40])
    ad_link.short_description = "Объявление"

    def messages_count(self, obj):
        return obj.messages.count()
    messages_count.short_description = "Сообщений"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("ad", "buyer", "seller").annotate(_count=Count("messages"))


# ─── СООБЩЕНИЯ ──────────────────────────────────────────────────────────────

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "chat_id", "sender", "short_text", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("sender__username", "text")
    ordering = ("-created_at",)
    raw_id_fields = ("chat", "sender")

    def short_text(self, obj):
        return obj.text[:60] + "…" if obj.text and len(obj.text) > 60 else (obj.text or "[фото]")
    short_text.short_description = "Текст"


# ─── ПЛАТЕЖИ ────────────────────────────────────────────────────────────────

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "ad_link", "amount_fmt", "days", "status_badge", "created_at")
    list_filter = ("status", "created_at")
    search_fields = ("user__username", "ad__title", "external_id")
    ordering = ("-created_at",)
    readonly_fields = ("created_at",)
    raw_id_fields = ("user", "ad")

    def ad_link(self, obj):
        return format_html('<a href="/admin/ads/ad/{}/change/">{}</a>', obj.ad.id, obj.ad.title[:40])
    ad_link.short_description = "Объявление"

    def amount_fmt(self, obj):
        return f"{obj.amount:,} ₸".replace(",", " ")
    amount_fmt.short_description = "Сумма"
    amount_fmt.admin_order_field = "amount"

    def status_badge(self, obj):
        colors = {
            "paid":    ("#1a4a1a", "#81c784", "✔ Оплачено"),
            "pending": ("#4a3a00", "#ffd54f", "⏳ Ожидание"),
            "failed":  ("#4a1a1a", "#ef9a9a", "✖ Ошибка"),
        }
        bg, fg, label = colors.get(obj.status, ("#333", "#ccc", obj.status))
        return format_html(
            '<span style="background:{};color:{};padding:3px 10px;border-radius:20px;font-size:0.78rem;font-weight:600;">{}</span>',
            bg, fg, label
        )
    status_badge.short_description = "Статус"


# ─── ЗАГОЛОВКИ САЙТА ────────────────────────────────────────────────────────

admin.site.site_header = "⚡ FYND"
admin.site.site_title = "FYND Admin"
admin.site.index_title = "Панель управления"
