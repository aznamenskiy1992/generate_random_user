import pytest
from unittest.mock import patch, MagicMock
import random

from src.generate import generate_users


@pytest.mark.parametrize(
    "column, assert_call_arg, result",
    [
        ("first_name", ["John", "Mike", "Bob"], "John"),
        ("last_name", ["Doe", "Kahil", "Birken"], "Doe"),
        ("city", ["New York", "Los Angeles"], "New York"),
    ]
)
def test_generate_random_first_last_name_and_cities_for_generate_users(column, assert_call_arg, result):
    """Тестирует генерацию случайного имени, фамилии и города из полученных списков"""
    with patch('random.choice') as mock_random_choice:
        mock_random_choice.return_value = result

        generator = generate_users(
            ["John", "Mike", "Bob"],
            ["Doe", "Kahil", "Birken"],
            ["New York", "Los Angeles"]
        )

        assert next(generator)[column] == result

        mock_random_choice.assert_any_call(assert_call_arg)
