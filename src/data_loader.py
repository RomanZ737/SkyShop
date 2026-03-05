import json
import logging
import os
from typing import Any

import pandas as pd

# Путь к папке с лог-файлами
LOG_FILE_PATH = os.path.join(os.path.dirname(__file__), "../logs/")

# Путь к папке с файлами данных
DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), "../data/")

data_file_name = "products.json"

logger = logging.getLogger("data_loader")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(filename=LOG_FILE_PATH + "data_loader.log", mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_data(data_source: str = 'json') -> Any:
    """
    На вход ничего не принимает,
    возвращает список словарей с данными транзакций
    Переменные пути файли и вида источника данных заданы в шапке модуля
    """
    if data_source == 'json':
        return data_loader_json(DATA_FILE_PATH + data_file_name)
    elif data_source == 'xlsx':
        return data_loader_xlsx(DATA_FILE_PATH + data_file_name)
    else:
        return []


def data_loader_json(file_path: str = "") -> Any:
    """
    Функция принимает путь к файлу (если данные будут загружаться из файла)
    и источник данных, возвращает список словарей с транзакциями
    """
    try:
        with open(file_path, encoding="utf-8") as json_file:
            data = json.load(json_file)
            logger.info(f"Файл {file_path} успешно открыт")
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        print("Ошибка: ", e)
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Ошибка: {e}")
        print("Ошибка: ", e)
        return []
    except TypeError as e:
        logger.error(f"Ошибка: {e}")
        print("Ошибка: ", e)
        return []
    except KeyError as e:
        logger.error(f"Ошибка: {e}")
        print("Ошибка: ", e)
        return []
    return data


def data_loader_xlsx(file_path: str = "") -> list:
    """
    Функция принимает путь к файлу (если данные будут загружаться из файла)
    и источник данных, возвращает список словарей с транзакциями
    """
    logger.info(f"Открываем файл XLSX с транзакциями {file_path}")
    try:
        excel_data = pd.read_excel(file_path)
        logger.info(f"Файл XLSX {file_path} успешно открыт")
    except FileNotFoundError as e:
        logger.error(f"Ошибка: {e}")
        return []
    except TypeError as e:
        logger.error(f"Ошибка: {e}")
        return []
    except Exception as e:
        logger.error(f"Ошибка: {e}")
        return []
    return excel_data.to_dict("records")
