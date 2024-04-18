import requests
from decouple import config

def check_bot_status():
    bot_token = config('BOT_TOKEN')
    url = f"https://api.telegram.org/bot{bot_token}/getMe"
    response = requests.get(url)
    data = response.json()
    print(data)
    if response.status_code == 200 and data['ok']:
        print("Bot is running!")
    else:
        print("Bot is not running!")

if __name__ == '__main__':
    check_bot_status()
