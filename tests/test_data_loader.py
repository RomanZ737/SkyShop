from unittest.mock import mock_open, patch

from src.data_loader import DATA_FILE_PATH, data_loader_json, get_data


def test_json_rise_error(wrong_data_for_json_file_open: str) -> None:
    mock_open_file = mock_open(read_data=wrong_data_for_json_file_open)
    with patch("src.data_loader.open", mock_open_file):
        result = data_loader_json(DATA_FILE_PATH + "products.json")
        assert str(result) == "[]"
        mock_open_file.assert_called_once_with(DATA_FILE_PATH + "products.json", encoding="utf-8")

    # mock_open_file = mock_open(read_data=wrong_data_for_json_file_open_2)
    # with patch("src.data_loader.open", mock_open_file):
    #     result = data_loader_json(DATA_FILE_PATH + "products.json")
    #     assert str(result) == '[]'
    #     mock_open_file.assert_called_once_with(DATA_FILE_PATH + "products.json", encoding="utf-8")


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
