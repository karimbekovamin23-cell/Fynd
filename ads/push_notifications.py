import json
from django.conf import settings


def send_push(user, title, body, url="/chats/"):
    if not settings.VAPID_PRIVATE_KEY:
        return
    try:
        from pywebpush import webpush, WebPushException
        from .models import PushSubscription
    except ImportError:
        return

    for sub in PushSubscription.objects.filter(user=user):
        try:
            webpush(
                subscription_info={
                    "endpoint": sub.endpoint,
                    "keys": {"p256dh": sub.p256dh, "auth": sub.auth},
                },
                data=json.dumps({"title": title, "body": body, "url": url}),
                vapid_private_key=settings.VAPID_PRIVATE_KEY,
                vapid_claims={"sub": f"mailto:{settings.VAPID_EMAIL}"},
            )
        except Exception as ex:
            resp = getattr(ex, "response", None)
            if resp is not None and resp.status_code in (404, 410):
                sub.delete()
