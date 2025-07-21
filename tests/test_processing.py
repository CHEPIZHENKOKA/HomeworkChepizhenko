import pytest
from src.processing import filter_by_state, sort_by_date


# Фикстура с тестовыми данными
@pytest.fixture
def sample_data():
    return [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
        {'id': 123456789, 'state': 'PENDING'},  # Элемент без даты
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [41428829, 939719570]),
    ("CANCELED", [594226727, 615064591]),
    ("PENDING", [123456789]),
    ("UNKNOWN", []),
    ("", []),  # Пустая строка
])
def test_filter_by_state(sample_data, state, expected_ids):
    """Тестирование фильтрации по состоянию транзакции"""
    result = filter_by_state(sample_data, state)
    assert [item['id'] for item in result] == expected_ids


# Тесты для sort_by_date
def test_sort_by_date_descending(sample_data):
    """Тестирование сортировки по убыванию даты (по умолчанию)"""
    # Фильтруем только элементы с датой
    data_with_date = [item for item in sample_data if 'date' in item]

    result = sort_by_date(data_with_date)
    dates = [item['date'] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_ascending(sample_data):
    """Тестирование сортировки по возрастанию даты"""
    # Фильтруем только элементы с датой
    data_with_date = [item for item in sample_data if 'date' in item]

    result = sort_by_date(data_with_date, ascending=True)
    dates = [item['date'] for item in result]
    assert dates == sorted(dates)


def test_sort_by_date_empty_list():
    """Тестирование сортировки пустого списка"""
    assert sort_by_date([]) == []
    assert sort_by_date([], ascending=True) == []


def test_sort_by_date_missing_key(sample_data):
    """Тестирование обработки элементов без даты"""
    result = sort_by_date(sample_data)

    # Проверяем что элементы без даты исключены
    assert len(result) == 4
    assert all('date' in item for item in result)

    # Проверяем порядок сортировки
    dates = [item['date'] for item in result]
    assert dates == sorted(dates, reverse=True)


def test_sort_by_date_single_element():
    """Тестирование сортировки списка с одним элементом"""
    data = [{'id': 1, 'date': '2023-01-01T00:00:00'}]
    assert sort_by_date(data) == data


# Тесты на граничные случаи
def test_filter_empty_list():
    """Тестирование фильтрации пустого списка"""
    assert filter_by_state([], "EXECUTED") == []


def test_sort_with_identical_dates():
    """Тестирование сортировки с одинаковыми датами"""
    data = [
        {'id': 1, 'date': '2023-01-01T00:00:00'},
        {'id': 2, 'date': '2023-01-01T00:00:00'},
        {'id': 3, 'date': '2023-01-01T00:00:00'}
    ]
    result = sort_by_date(data)
    assert [item['id'] for item in result] == [1, 2, 3]  # Сохраняют исходный порядок при стабильной сортировке