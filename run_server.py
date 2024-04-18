import subprocess
import threading

def run_django():
    subprocess.run(["daphne", "--bind", "0.0.0.0", "--port", "8888", "web_core.asgi:application"])

# def run_bot():
#     subprocess.run(["python", "run_bot.py"])

if __name__ == "__main__":
    django_thread = threading.Thread(target=run_django)
    django_thread.start()

    # bot_thread = threading.Thread(target=run_bot)
    # bot_thread.start()

    # django_thread.join()
    # bot_thread.join()
