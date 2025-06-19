import pytest
from unittest.mock import patch

from main import main


@patch('main.generate_users')
@patch('builtins.input')
def test_print_group_random_users_to_console_from_main(mock_input, mock_generate_users, capsys):
    """Тестирует вывод сгенерированной группы пользователей в консоль"""
    mock_input.return_value = "test"

    mock_generate_users.return_value = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 25,
        "city": "New York"
    }

    main(2)

    captured = capsys.readouterr()
    assert captured.out == str([
        {
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "city": "New York"
        },
        {
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "city": "New York"
        },
    ])+"\n"
