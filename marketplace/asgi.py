import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'marketplace.settings')

import django
django.setup()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application

import ads.routing

application = ProtocolTypeRouter({
    
    "http": get_asgi_application(),

    "websocket": AuthMiddlewareStack(
        URLRouter(
            ads.routing.websocket_urlpatterns
        )
    ),

})