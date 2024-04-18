"""
ASGI config for web_core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os
from channels.routing import ProtocolTypeRouter
from django.core.asgi import get_asgi_application

from bot_core.application_core.bot import main
from django.conf import settings

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
import bot_core.routing


async def start_bot():
    main()


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_core.settings')

# from channels.routing import ProtocolTypeRouter
django_asgi_app = get_asgi_application()

application = ProtocolTypeRouter(
    {
        "http": django_asgi_app,
        "websocket": AuthMiddlewareStack(URLRouter(bot_core.routing.websocket_urlpatterns)),
    }
)


