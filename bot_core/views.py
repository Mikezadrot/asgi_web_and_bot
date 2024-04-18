from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from django.contrib.auth.decorators import login_required


from django.shortcuts import render
import json

@login_required
def bot_status_view(request):
    user = request.user
    client_ip = request.META

    context = {
        "user": user,
        "client_ip": client_ip,
    }

    return render(request, 'bot_status.html', context=context)

    # return render(request, 'bot_status.html', {'bot_status': bot_status})

#
# async def start_bot():
#     channel_layer = get_channel_layer()
#
#     # Відправити повідомлення усім підключеним клієнтам
#     channel_layer.group_send(
#         'bot_status_group',  # Група WebSocket
#         {
#             'type': 'bot.status',  # Тип повідомлення
#             'status': 'active'  # Статус бота
#         }
#     )
#
#
# # return render(request, 'your_template.html')
#
#
# async def stop_bot():
#     # Код для зупинки бота
#     channel_layer = get_channel_layer()
#     channel_layer.group_send(
#         'bot_status_group',
#         {
#             'type': 'bot.status',
#             'status': 'offline'
#         }
#     )
#     # return render(request, 'your_template.html')
