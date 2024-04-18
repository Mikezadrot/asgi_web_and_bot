import subprocess
import threading
import time
import logging

# Налаштування логування у файл
logging.basicConfig(filename='control_panel.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_django():
    subprocess.run(["daphne", "--bind", "0.0.0.0", "--port", "8888", "web_core.asgi:application"])

def run_bot():
    subprocess.run(["python", "run_bot.py"])

if __name__ == "__main__":
    # django_thread = threading.Thread(target=run_django)
    # django_thread.start()

    django_thread = None
    bot_thread = None

    while True:
        command = input("Enter command (start bot/stop bot/start server/stop server/exit): ")
        logging.info(f"Received command: {command}")  # Записуємо команду у файл

        if command == "start bot" and bot_thread is None:
            bot_thread = threading.Thread(target=run_bot)
            bot_thread.start()
            logging.info("Bot started.")
        elif command == "stop bot" and bot_thread is not None:
            subprocess.run(["pkill", "-f", "run_bot.py"])
            bot_thread.join()
            bot_thread = None
            logging.info("Bot stopped.")
        elif command == "start server":
            subprocess.run(["pkill", "-f", "daphne"])
            django_thread = threading.Thread(target=run_django)
            django_thread.start()
            logging.info("Server started.")
        elif command == "stop server":
            subprocess.run(["pkill", "-f", "daphne"])
            logging.info("Server stopped.")
        elif command == "exit":
            if bot_thread is not None:
                subprocess.run(["pkill", "-f", "run_bot.py"])
                bot_thread.join()
            subprocess.run(["pkill", "-f", "daphne"])
            django_thread.join()
            logging.info("Exiting control panel.")
            break
        else:
            logging.warning("Invalid command entered.")
            print("Invalid command. Please enter 'start bot', 'stop bot', 'start server', 'stop server', or 'exit'.")
