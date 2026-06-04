from django.conf import settings


def push_config(request):
    return {
        "vapid_public_key": getattr(settings, "VAPID_PUBLIC_KEY", ""),
    }
