import random
from typing import Iterator


def generate_users(first_names: list, last_names: list, cities: list) -> Iterator[dict]:
    """
    Генерирует бесконечную последовательность случайных пользователей на основе переданных данных.

    Параметры:
        first_names (list): Список возможных имен пользователей
        last_names (list): Список возможных фамилий пользователей
        cities (list): Список возможных городов проживания

    Возвращает:
        Iterator[dict]: Бесконечный итератор словарей с данными пользователей. Каждый словарь содержит:
            - first_name (str): Случайное имя из списка first_names
            - last_name (str): Случайная фамилия из списка last_names
            - age (int): Случайный возраст от 18 до 65 лет
            - city (str): Случайный город из списка cities

    Исключения:
        TypeError: Если любой из аргументов не является списком

    Особенности:
        - Проверяет тип всех входных аргументов
        - Генерирует пользователей бесконечно при итерации
        - Возраст генерируется случайно в диапазоне 18-65 лет
        - Использует random.choice для случайного выбора элементов

    Пример использования:
        >>> user_gen = generate_users(["Иван", "Петр"], ["Иванов", "Петров"], ["Москва", "Сочи"])
        >>> next(user_gen)
        {'first_name': 'Петр', 'last_name': 'Иванов', 'age': 42, 'city': 'Москва'}
    """
    # Проверяем, что все аргументы являются списками
    invalid_args: list = [
        name
        for name, arg in zip(["first_names", "last_names", "cities"], [first_names, last_names, cities])
        if not isinstance(arg, list)
    ]

    # Если есть некорректные аргументы - вызываем исключение
    if invalid_args:
        raise TypeError(f"Аргументы должны быть переданы в списках. Не в списках: {", ".join(invalid_args)}")

    # Бесконечный цикл генерации пользователей
    while True:
        # Создаем словарь с данными пользователя
        generated_user: dict = {
            "first_name": random.choice(first_names),  # Случайное имя
            "last_name": random.choice(last_names),    # Случайная фамилия
            "age": random.randint(18, 65),            # Случайный возраст 18-65
            "city": random.choice(cities),            # Случайный город
        }
        # Возвращаем пользователя через yield
        yield generated_user
