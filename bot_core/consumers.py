# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
import json
from decouple import config
import websockets
# from .views import start_bot, stop_bot
from channels.layers import get_channel_layer
from urllib.parse import parse_qs





allowed_tokens = {
    f"{config('BOT_TOKEN')}": f"{config('BOT_TOKEN')}",
    f"{config('BOT_TOKEN_SENDER')}": f"{config('BOT_TOKEN_SENDER')}",

    "1": "1",
}

status_bota = None


usvery = {}
user_name_ip = {}

async def start_bot():
    channel_layer = get_channel_layer()

    # Відправити повідомлення усім підключеним клієнтам
    channel_layer.group_send(
        'bot_status_group',  # Група WebSocket
        {
            'type': 'bot.status',  # Тип повідомлення
            'status': 'active'  # Статус бота
        }
    )
    print("func start bot worked")

# return render(request, 'your_template.html')


async def stop_bot():
    # Код для зупинки бота
    channel_layer = get_channel_layer()
    channel_layer.group_send(
        'bot_status_group',
        {
            'type': 'bot.status',
            'status': 'offline'
        }
    )
    # return render(request, 'your_template.html')



class BotConnect(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

        await self.send(text_data="Enter token")

    async def disconnect(self, close_code):
        print(f"Disconnected with code: {close_code}")


    async def receive(self, text_data=None, bytes_data=None):
        print(f'taken data: {text_data}')
        # datas = hasattr(self, 'ip')
        # print(self)
        if hasattr(self, 'token_accepted') and self.token_accepted:
            # Якщо токен вже був прийнятий, продовжуємо отримувати повідомлення від клієнта
            # Тут ви можете реалізувати логіку для обробки наступних повідомлень
            # print(f'taken data: {text_data}')
            await self.send(text_data)

            if str(text_data) == "Bot start work":
                print("Bot starting")
                await start_bot()
            elif str(text_data) == "Bot stop work":
                print("Bot stoping")
                await stop_bot()

        else:
            token = text_data
            # print(token)
            if token in allowed_tokens:
                await self.send(text_data="Token accepted")
                self.token_accepted = True
                # datass = self.scope
                # print(datass)
            else:
                await self.send("Dont accept")
                await self.close()


class BotStatusConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        # Додати користувача до списку онлайн користувачів
        await self.channel_layer.group_add('online_users', self.channel_name)

        # print(self.channel_name)
        query_params = parse_qs(self.scope['query_string'].decode('utf-8'))
        user_name = query_params.get('user_name', [''])[0]
        user_ip = query_params.get('user_ip', [''])[0]

        users = self.scope.get('users', {})
        users[self.channel_name] = user_name

        usvery[self.channel_name] = user_name
        user_name_ip[self.channel_name] = {
            'name': user_name,
            'ip': user_ip

        }


        self.scope['users'] = users
        # Отримати список онлайн користувачів та відправити його
        await self.send_online_users()


        # print(users)

    async def disconnect(self, close_code):
        # Видалити користувача зі списку онлайн користувачів
        await self.channel_layer.group_discard('online_users', self.channel_name)

        users = self.scope.get('users', {})
        users.pop(self.channel_name, None)
        self.scope['users'] = users
        key = self.channel_name
        usvery.__delitem__(key)
        user_name_ip.__delitem__(key)
        # Оновити список онлайн користувачів та відправити його
        await self.send_online_users()

    async def receive(self, text_data=None, bytes_data=None):
        if text_data == 'update_count':
            await self.send_online_users()
        else:
            pass

    async def bot_status_changed(self, event):
        pass

    async def send_online_users(self):

        users = self.scope.get('users')
        print(usvery)
        print(user_name_ip)
        online_users_names = list(set(usvery.values()))

        if "AnonymousUser" in usvery.values():
            count = len(set(usvery.values())) - 1
            online_users_names.remove("AnonymousUser")

        else:
            count = len(set(usvery.values()))



        # print(users)
        # Отримати всіх підключених користувачів у групі
        group_name = 'online_users'
        group_members = self.channel_layer.groups.get(group_name, set())

        # print(group_members)

        online_users = count
        # Відправити кількість онлайн користувачів на клієнтську сторону
        await self.send(text_data=json.dumps({'online_users': online_users,
                                              'online_users_names': user_name_ip
                                              }))


    async def online_users_count(self, event):
        await self.send(text_data=json.dumps({'online_users': event['online_users']}))
