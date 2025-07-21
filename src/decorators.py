import functools
from typing import Callable, Optional, Any

def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функций
    filename: Имя файла для записи логов (None - вывод в консоль)
    return: Декорированная функция
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                _write_log(f"{func.__name__} ok", filename)
                return result
            except Exception as e:
                _write_log(
                    f"{func.__name__} error: {type(e).__name__}. "
                    f"Inputs: {args}, {kwargs}",
                    filename
                )
                raise
        return wrapper
    return decorator

def _write_log(message: str, filename: Optional[str] = None) -> None:
    """Вспомогательная функция для записи логов"""
    if filename:
        with open(filename, 'a', encoding='utf-8') as file:
            file.write(message + '\n')
    else:
        print(message)
