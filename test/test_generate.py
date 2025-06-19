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


@patch('random.randint')
def test_generate_random_age_for_generate_users(mock_random_randint):
    """Тестирует генерацию случайного возраста из диапазона 18-65 лет"""
    mock_random_randint.return_value = 25

    generator = generate_users(
        ["John", "Mike", "Bob"],
        ["Doe", "Kahil", "Birken"],
        ["New York", "Los Angeles"]
    )

    assert next(generator)["age"] == 25

    mock_random_randint.assert_called_once_with(18, 65)


@pytest.mark.parametrize(
    "first_name, last_name, city, raise_message",
    [
        ("John", ["Doe", "Kahil", "Birken"], ["New York", "Los Angeles"], "Аргументы должны быть переданы в списках. Не в списках: first_names"),
        (["John", "Mike", "Bob"], "Doe", ["New York", "Los Angeles"], "Аргументы должны быть переданы в списках. Не в списках: last_names"),
        (["John", "Mike", "Bob"], ["Doe", "Kahil", "Birken"], "New York", "Аргументы должны быть переданы в списках. Не в списках: cities"),
        ("John", "Doe", "New York", "Аргументы должны быть переданы в списках. Не в списках: first_names, last_names, cities"),
    ]
)
def test_incorrect_arg_type_for_generate_users(first_name, last_name, city, raise_message):
    """Тестирует обработку ошибки, когда аргументы переданы не в списках"""
    with pytest.raises(TypeError) as exc_info:
        next(generate_users(first_name, last_name, city))
    assert str(exc_info.value) == raise_message
