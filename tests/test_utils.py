import pytest
import json
import tempfile
import os
from src.utils import load_json_data


def test_load_valid_json_data():
    """Тест загрузки валидного JSON-файла"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
        data = [{"id": 1, "name": "Test"}, {"id": 2, "name": "Example"}]
        json.dump(data, tmp)
        tmp_path = tmp.name

    result = load_json_data(tmp_path)
    os.unlink(tmp_path)
    assert result == data


def test_load_empty_json_data():
    """Тест загрузки пустого JSON-файла"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
        tmp.write('')
        tmp_path = tmp.name

    result = load_json_data(tmp_path)
    os.unlink(tmp_path)
    assert result == []


def test_load_invalid_json_data():
    """Тест загрузки невалидного JSON"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
        tmp.write('{"invalid": json')
        tmp_path = tmp.name

    result = load_json_data(tmp_path)
    os.unlink(tmp_path)
    assert result == []


def test_load_non_list_json_data():
    """Тест загрузки JSON, который не является списком"""
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as tmp:
        json.dump({"key": "value"}, tmp)
        tmp_path = tmp.name

    result = load_json_data(tmp_path)
    os.unlink(tmp_path)
    assert result == []


def test_load_nonexistent_file():
    """Тест загрузки несуществующего файла"""
    result = load_json_data("non_existent_file.json")
    assert result == []
    