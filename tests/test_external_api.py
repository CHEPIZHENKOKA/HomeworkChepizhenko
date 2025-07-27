import pytest
from unittest.mock import patch, MagicMock
from src.external_api import convert_amount_to_rub


@patch('src.external_api.requests.get')
@patch('src.external_api.os.getenv')
def test_convert_rub_transaction(mock_getenv, mock_get):
    """Тест конвертации RUB транзакции"""
    transaction = {
        'operationAmount': {
            'amount': '100.0',
            'currency': {'code': 'RUB'}
        }
    }
    result = convert_amount_to_rub(transaction)
    assert result == 100.0
    mock_get.assert_not_called()


@patch('src.external_api.requests.get')
@patch('src.external_api.os.getenv')
def test_convert_usd_transaction(mock_getenv, mock_get):
    """Тест конвертации USD транзакции с моком API"""
    # Настройка моков
    mock_getenv.return_value = 'test_api_key'
    mock_response = MagicMock()
    mock_response.json.return_value = {'rates': {'RUB': 75.0}}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '10.0',
            'currency': {'code': 'USD'}
        }
    }
    result = convert_amount_to_rub(transaction)
    assert result == 750.0
    mock_get.assert_called_once()


@patch('src.external_api.requests.get')
@patch('src.external_api.os.getenv')
def test_convert_eur_transaction(mock_getenv, mock_get):
    """Тест конвертации EUR транзакции с моком API"""
    # Настройка моков
    mock_getenv.return_value = 'test_api_key'
    mock_response = MagicMock()
    mock_response.json.return_value = {'rates': {'RUB': 85.0}}
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    transaction = {
        'operationAmount': {
            'amount': '20.0',
            'currency': {'code': 'EUR'}
        }
    }
    result = convert_amount_to_rub(transaction)
    assert result == 1700.0
    mock_get.assert_called_once()


@patch('src.external_api.requests.get')
@patch('src.external_api.os.getenv')
def test_convert_other_currency(mock_getenv, mock_get):
    """Тест конвертации транзакции в другой валюте"""
    transaction = {
        'operationAmount': {
            'amount': '50.0',
            'currency': {'code': 'GBP'}
        }
    }
    result = convert_amount_to_rub(transaction)
    assert result == 50.0
    mock_get.assert_not_called()


from unittest.mock import patch


@patch('src.external_api.requests.get')
def test_convert_api_key_missing(mock_get):
    """Тест отсутствия API ключа"""
    # Настраиваем поведение заглушки, например, возвращаем None или исключение
    mock_get.return_value.json.return_value = {}  # Эмуляция ответа без данных
    transaction = {
        'operationAmount': {
            'amount': '10.0',
            'currency': {'code': 'USD'}
        }
    }
    result = convert_amount_to_rub(transaction)
    assert result is None


@patch('src.external_api.requests.get')
@patch('src.external_api.os.getenv')
def test_convert_api_failure(mock_getenv, mock_get):
    """Тест сбоя API"""
    mock_getenv.return_value = 'test_api_key'
    mock_get.side_effect = Exception("API error")

    transaction = {
        'operationAmount': {
            'amount': '10.0',
            'currency': {'code': 'USD'}
        }
    }
    result = convert_amount_to_rub(transaction)
    assert result is None


def test_convert_invalid_transaction():
    """Тест невалидной транзакции"""
    transaction = {'invalid': 'data'}
    result = convert_amount_to_rub(transaction)
    assert result is None
