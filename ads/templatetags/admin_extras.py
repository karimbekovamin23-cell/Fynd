from django import template
from django.db.models import Sum
from django.utils import timezone

register = template.Library()


@register.filter
def space_fmt(value):
    try:
        return f"{int(value):,}".replace(",", " ")
    except (ValueError, TypeError):
        return value


@register.inclusion_tag("admin/stats_cards.html")
def admin_stats():
    from django.contrib.auth.models import User
    from ads.models import Ad, Payment, Message, Chat

    return {
        "ads_total": Ad.objects.count(),
        "ads_published": Ad.objects.filter(is_published=True).count(),
        "ads_moderation": Ad.objects.filter(is_published=False).count(),
        "users_total": User.objects.count(),
        "payments_paid": Payment.objects.filter(status="paid").count(),
        "revenue": Payment.objects.filter(status="paid").aggregate(t=Sum("amount"))["t"] or 0,
        "messages_today": Message.objects.filter(created_at__date=timezone.now().date()).count(),
        "chats_total": Chat.objects.count(),
    }
