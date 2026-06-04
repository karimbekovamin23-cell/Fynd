import os
import requests as http

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "")

_API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def send_moderation_alert(ad):
    if not BOT_TOKEN or not ADMIN_CHAT_ID:
        return

    first_image = ad.images.first()
    price = f"{ad.price:,}".replace(",", " ")

    text = (
        f"📋 *Новое объявление на модерации*\n\n"
        f"*{ad.title}*\n"
        f"💰 {price} ₸\n"
        f"🏙 {ad.city or '—'}\n"
        f"👤 [{ad.author.username}](https://www.fynd.moscow/profile/{ad.author.username}/)\n"
        f"🔗 [Открыть в Django-admin](https://www.fynd.moscow/admin/ads/ad/{ad.pk}/change/)"
    )

    keyboard = {"inline_keyboard": [[
        {"text": "✔ Одобрить", "callback_data": f"approve_{ad.pk}"},
        {"text": "✖ Отклонить", "callback_data": f"reject_{ad.pk}"},
    ]]}

    try:
        if first_image and first_image.image:
            http.post(
                f"{_API}/sendPhoto",
                json={
                    "chat_id": ADMIN_CHAT_ID,
                    "photo": first_image.image.url,
                    "caption": text,
                    "parse_mode": "Markdown",
                    "reply_markup": keyboard,
                },
                timeout=5,
            )
        else:
            http.post(
                f"{_API}/sendMessage",
                json={
                    "chat_id": ADMIN_CHAT_ID,
                    "text": text,
                    "parse_mode": "Markdown",
                    "reply_markup": keyboard,
                    "disable_web_page_preview": True,
                },
                timeout=5,
            )
    except Exception:
        pass
