import os
import requests as http

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "")
ADMIN_CHAT_ID = os.getenv("TELEGRAM_ADMIN_CHAT_ID", "")

_API = f"https://api.telegram.org/bot{BOT_TOKEN}"


def _call(method, **kwargs):
    try:
        http.post(f"{_API}/{method}", json=kwargs, timeout=5)
    except Exception:
        pass


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


# ── Helpers ───────────────────────────────────────────────────────────────────

def _status(ad):
    if not ad.is_published:
        return "⏳"
    label = "✅"
    if ad.is_pinned:
        label += "📌"
    if ad.is_promoted:
        label += f"🚀{ad.promotion_level}"
    return label


def _detail_text(ad):
    price = f"{ad.price:,}".replace(",", " ")
    promo_line = ""
    if ad.is_promoted and ad.promoted_until:
        until = ad.promoted_until.strftime("%d.%m.%Y")
        promo_line = f"\n🚀 Продвижение до {until} (ур. {ad.promotion_level})"
    return (
        f"{_status(ad)} *{ad.title}*\n"
        f"💰 {price} ₸\n"
        f"🏙 {ad.city or '—'}\n"
        f"👤 {ad.author.username}\n"
        f"📅 {ad.created_at.strftime('%d.%m.%Y')}"
        f"{promo_line}"
    )


def _detail_keyboard(ad):
    pk = ad.pk
    pin_btn = (
        {"text": "📌 Открепить", "callback_data": f"unpin_{pk}"}
        if ad.is_pinned
        else {"text": "📌 Закрепить", "callback_data": f"pin_{pk}"}
    )
    pause_btn = (
        {"text": "⏸ Приостановить", "callback_data": f"pause_{pk}"}
        if ad.is_published
        else {"text": "▶ Возобновить", "callback_data": f"resume_{pk}"}
    )
    return {"inline_keyboard": [
        [pin_btn, {"text": "🚀 Продвижение", "callback_data": f"promo_{pk}"}],
        [pause_btn, {"text": "🗑 Удалить", "callback_data": f"del_{pk}"}],
        [{"text": "◀ К списку", "callback_data": "list_0"}],
    ]}


# ── Public send functions ──────────────────────────────────────────────────────

def send_ad_list(chat_id, message_id=None):
    from ads.models import Ad
    ads = list(Ad.objects.order_by("-created_at")[:20])

    if not ads:
        text = "📋 Объявлений нет"
        keyboard = {"inline_keyboard": []}
    else:
        lines = []
        buttons = []
        for ad in ads:
            price = f"{ad.price:,}".replace(",", " ")
            lines.append(f"{_status(ad)} {ad.title[:30]} — {price} ₸")
            buttons.append([{
                "text": f"👁 {ad.title[:28]}",
                "callback_data": f"detail_{ad.pk}",
            }])
        text = "📋 *Список объявлений* (последние 20)\n\n" + "\n".join(lines)
        keyboard = {"inline_keyboard": buttons}

    if message_id:
        _call("editMessageText",
              chat_id=chat_id, message_id=message_id,
              text=text, parse_mode="Markdown", reply_markup=keyboard)
    else:
        _call("sendMessage",
              chat_id=chat_id,
              text=text, parse_mode="Markdown", reply_markup=keyboard)


def send_ad_detail(chat_id, ad, message_id=None):
    text = _detail_text(ad)
    keyboard = _detail_keyboard(ad)
    if message_id:
        _call("editMessageText",
              chat_id=chat_id, message_id=message_id,
              text=text, parse_mode="Markdown", reply_markup=keyboard)
    else:
        _call("sendMessage",
              chat_id=chat_id,
              text=text, parse_mode="Markdown", reply_markup=keyboard)


def send_promo_keyboard(chat_id, ad, message_id=None):
    pk = ad.pk
    text = f"🚀 *Продвижение*\n«{ad.title[:40]}»\n\nВыберите уровень и срок:"
    keyboard = {"inline_keyboard": [
        [
            {"text": "🚀 Ур.1 — 7 дней",   "callback_data": f"p1_{pk}"},
            {"text": "🚀🚀 Ур.2 — 14 дней", "callback_data": f"p2_{pk}"},
        ],
        [
            {"text": "🚀🚀🚀 Ур.3 — 30 дней", "callback_data": f"p3_{pk}"},
            {"text": "❌ Убрать",            "callback_data": f"p0_{pk}"},
        ],
        [{"text": "◀ Назад", "callback_data": f"detail_{pk}"}],
    ]}
    if message_id:
        _call("editMessageText",
              chat_id=chat_id, message_id=message_id,
              text=text, parse_mode="Markdown", reply_markup=keyboard)
    else:
        _call("sendMessage",
              chat_id=chat_id,
              text=text, parse_mode="Markdown", reply_markup=keyboard)
