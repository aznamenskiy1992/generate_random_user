import pytest
from unittest.mock import patch, MagicMock
import random

from src.generate import generate_users


@patch('random.choice')
def test_generate_random_first_name_for_generate_users(mock_random_choice):
    """Тестирует генерацию случайного имени из полученного списка"""
    mock_random_choice.return_value = "John"

    generator = generate_users(
        ["John", "Mike", "Bob"],
        ["Doe", "Kahil", "Birken"],
        ["New York", "Los Angeles"]
    )

    assert next(generator)["first_name"] == "John"

    mock_random_choice.assert_any_call(["John", "Mike", "Bob"])