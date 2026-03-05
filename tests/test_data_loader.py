import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.data_loader import DATA_FILE_PATH, data_loader_json, data_loader_xlsx, get_data


@patch("src.data_loader.pd.read_excel")
def test_xlsx_loader(mock_read_excel: unittest.mock.Mock) -> None:
    """
    Тестируем функцию json_loader. Функция принимает на вход
    путь до XLSX-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не
    список или не найден, функция возвращает пустой список
    """
    mock_df = pd.DataFrame({"existing_col": [1, 2, 3]})
    mock_read_excel.return_value = mock_df
    result_df = pd.DataFrame(data_loader_xlsx("transactions_excel.xlsx"))
    mock_read_excel.assert_called()
    expected_df = pd.DataFrame({"existing_col": [1, 2, 3]})
    pd.testing.assert_frame_equal(result_df, expected_df)


def test_xlsx_load_empty() -> None:
    """
    Проверяем передачу неверного пути к файлу для функции data_loader_xlsx
    """
    assert data_loader_xlsx("empty.xlsx") == []


def test_json_rise_error(wrong_data_for_json_file_open: str, wrong_data_for_json_file_open_2: str) -> None:
    mock_open_file = mock_open(read_data=wrong_data_for_json_file_open)
    with patch("src.data_loader.open", mock_open_file):
        result = data_loader_json(DATA_FILE_PATH + "products.json")
        assert str(result) == '[]'
        mock_open_file.assert_called_once_with(DATA_FILE_PATH + "products.json", encoding="utf-8")

    mock_open_file = mock_open(read_data=wrong_data_for_json_file_open_2)
    with patch("src.data_loader.open", mock_open_file):
        result = data_loader_json(DATA_FILE_PATH + "products.json")
        assert str(result) == '[]'
        mock_open_file.assert_called_once_with(DATA_FILE_PATH + "products.json", encoding="utf-8")


def test_get_json_data(data_for_json_file_open: str) -> None:
    """
    Тестируем функцию json_loader. Функция принимает на вход
    путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях. Если файл пустой, содержит не
    список или не найден, функция возвращает пустой список
    """
    mock_open_file = mock_open(read_data=data_for_json_file_open)
    with patch("src.data_loader.open", mock_open_file):
        result = data_loader_json(DATA_FILE_PATH + "products.json")
        assert str(result) == data_for_json_file_open.replace('"', "'")
        mock_open_file.assert_called_once_with(DATA_FILE_PATH + "products.json", encoding="utf-8")


def test_data_json_empty() -> None:
    """
    Проверяем передачу неверного пути к файлу для функции data_loader_xlsx
    """
    assert data_loader_json("empty.json") == []


def test_get_data() -> None:
    """
    Тестируем функцию get_data
    """
    assert get_data("xxxx") == []
