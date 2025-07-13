import pytest
from src.processing import filter_by_state, sort_by_date

# Фикстура с тестовыми данными
@pytest.fixture
def sample_data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2023-01-01T00:00:00.000000"},
        {"id": 2, "state": "PENDING", "date": "2023-01-02T00:00:00.000000"},
        {"id": 3, "state": "EXECUTED", "date": "2023-01-03T00:00:00.000000"},
        {"id": 4, "state": "CANCELED", "date": "2023-01-04T00:00:00.000000"},
        {"id": 5},  # Нет state и date
        {"id": 6, "state": "EXECUTED"},  # Нет date
        {"id": 7, "date": "2023-01-05T00:00:00.000000"},  # Нет state
    ]


# Тесты для filter_by_state
@pytest.mark.parametrize("state, expected_ids", [
    ("EXECUTED", [1, 3, 6]),    # Стандартный статус
    ("PENDING", [2]),        # Одиночный статус
    ("CANCELED", [4]),       # Другой статус
    ("UNKNOWN", []),         # Несуществующий статус
])
def test_filter_by_state(sample_data, state, expected_ids):
    result = filter_by_state(sample_data, state)
    assert [item["id"] for item in result] == expected_ids


# Тесты для sort_by_date
def test_sort_by_date_descending(sample_data):
    # Фильтруем элементы с датой
    valid_data = [item for item in sample_data if "date" in item]
    result = sort_by_date(valid_data)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates, reverse=True)

def test_sort_by_date_ascending(sample_data):
    valid_data = [item for item in sample_data if "date" in item]
    result = sort_by_date(valid_data, ascending=True)
    dates = [item["date"] for item in result]
    assert dates == sorted(dates)

def test_sort_by_date_with_duplicates():
    data = [
        {"date": "2023-01-01T00:00:00.000000"},
        {"date": "2023-01-01T00:00:00.000000"},  # Дубликат даты
        {"date": "2022-01-01T00:00:00.000000"},
    ]
    result = sort_by_date(data)
    assert [item["date"] for item in result] == [
        "2023-01-01T00:00:00.000000",
        "2023-01-01T00:00:00.000000",
        "2022-01-01T00:00:00.000000"
    ]