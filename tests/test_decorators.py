import pytest
import os
from typing import Callable, Any
from src.decorators import log  # Предполагается, что декоратор в src/decorators.py


# Тестовая функция для успешного выполнения
@log()
def successful_function(a: int, b: int) -> int:
    return a + b


# Тестовая функция, вызывающая исключение
@log()
def error_function(a: int, b: int) -> int:
    raise ValueError("Test error")


# Тестовая функция для записи в файл
@log(filename="test_log.txt")
def file_log_function(a: int, b: int) -> int:
    return a * b


def test_successful_console_log(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест успешного выполнения с выводом в консоль"""
    result = successful_function(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "successful_function ok" in captured.out


def test_error_console_log(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест ошибки с выводом в консоль"""
    with pytest.raises(ValueError):
        error_function(4, 5)

    captured = capsys.readouterr()
    assert "error_function error: ValueError" in captured.out
    assert "Inputs: (4, 5)" in captured.out


def test_successful_file_log() -> None:
    """Тест успешного выполнения с записью в файл"""
    # Удаляем предыдущий файл логов
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    result = file_log_function(3, 4)

    # Проверяем результат выполнения
    assert result == 12

    # Проверяем запись в файл
    with open("test_log.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        assert "file_log_function ok" in content


def test_error_file_log() -> None:
    """Тест ошибки с записью в файл"""
    # Удаляем предыдущий файл логов
    if os.path.exists("test_log.txt"):
        os.remove("test_log.txt")

    # Создаем функцию с ошибкой, записывающую в файл
    @log(filename="test_log.txt")
    def local_error_func(x: int) -> None:
        raise TypeError("Custom error")

    with pytest.raises(TypeError):
        local_error_func(10)

    # Проверяем запись в файл
    with open("test_log.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        assert "local_error_func error: TypeError" in content
        assert "Inputs: (10,)" in content


def test_log_preserves_function_metadata() -> None:
    """Тест сохранения метаданных функции"""

    @log()
    def sample_func(a: int) -> int:
        """Тестовая функция"""
        return a

    assert sample_func.__name__ == "sample_func"
    assert sample_func.__doc__ == "Тестовая функция"
    assert sample_func(5) == 5


def test_log_with_keyword_arguments(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест работы с ключевыми аргументами"""

    @log()
    def kw_func(a: int, b: int = 0) -> int:
        return a + b

    result = kw_func(5, b=3)
    captured = capsys.readouterr()

    assert result == 8
    assert "kw_func ok" in captured.out


def test_log_no_arguments(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест функции без аргументов"""

    @log()
    def no_args_func() -> str:
        return "test"

    result = no_args_func()
    captured = capsys.readouterr()

    assert result == "test"
    assert "no_args_func ok" in captured.out


def test_log_with_file_and_console(capsys: pytest.CaptureFixture[str]) -> None:
    """Тест одновременной работы с файлом и консолью"""
    if os.path.exists("mixed_log.txt"):
        os.remove("mixed_log.txt")

    @log(filename="mixed_log.txt")
    def mixed_func(x: str) -> str:
        return x.upper()

    result = mixed_func("hello")

    # Проверяем вывод в консоль (должен отсутствовать)
    captured = capsys.readouterr()
    assert captured.out == ""

    # Проверяем запись в файл
    with open("mixed_log.txt", 'r', encoding='utf-8') as f:
        content = f.read()
        assert "mixed_func ok" in content

    assert result == "HELLO"


# Очистка после тестов
def teardown_module() -> None:
    """Удаление тестовых файлов после выполнения тестов"""
    for filename in ["test_log.txt", "mixed_log.txt"]:
        if os.path.exists(filename):
            os.remove(filename)
