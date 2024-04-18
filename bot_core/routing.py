from django.urls import re_path
from bot_core import consumers

websocket_urlpatterns = [
    re_path(r'ws/connect/$', consumers.BotConnect.as_asgi()),
    re_path(r'ws/bot_status/$', consumers.BotStatusConsumer.as_asgi()),

]