import os
import requests
from typing import Dict, Union, Optional, Any
from dotenv import load_dotenv

load_dotenv()


def convert_amount_to_rub(transaction: Dict[str, Any]) -> Optional[float]:
    """Конвертирует сумму транзакции в рубли"""
    try:
        amount = float(transaction['operationAmount']['amount'])
        currency = transaction['operationAmount']['currency']['code']

        # Если валюта уже в рублях
        if currency == 'RUB':
            return amount

        # Для USD и EUR делаем конвертацию
        if currency in ('USD', 'EUR'):
            api_key = os.getenv('EXCHANGE_RATE_API_KEY')
            if not api_key:
                raise ValueError("API key not found in environment variables")

            url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
            response = requests.get(url, headers={'apikey': api_key})
            response.raise_for_status()

            rate = response.json()['rates']['RUB']
            return amount * rate

        # Для других валют возвращаем исходную сумму
        return amount
    except Exception:
        return None
