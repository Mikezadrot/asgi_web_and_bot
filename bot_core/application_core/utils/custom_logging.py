import logging
from logging.handlers import RotatingFileHandler
import sys


def setup_custom_logger(name):
    log_level = logging.INFO
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

    # Налаштування кореневого логера
    logging.basicConfig(level=log_level, stream=sys.stdout, format=log_format)

    # Додаткова настройка для зберігання логів в файл
    log_file = 'main.log'
    file_handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    file_handler.setFormatter(logging.Formatter(log_format))
    file_handler.setLevel(log_level)

    # Додайтеєм файловий обробник до кореневого логгера
    logging.getLogger().addHandler(file_handler)

    return logging.getLogger(name)