from typing import Iterator

from src.generate import generate_users


def main(cnt_generate_user: int) -> None:
    """Выводит сгенерированных пользователей в консоль в списке"""
    first_names: str = input("Введите имена пользователей через запятую")
    last_names: str = input("Введите фамилии пользователей через запятую")
    cities: str = input("Введите названия городов через запятую")

    if None in (first_names, last_names, cities):
        raise ValueError("Не введены параметры пользователя")

    first_names_split: list = first_names.split(",")
    last_names_split: list = last_names.split(",")
    cities_split: list = cities.split(",")

    generated_users: list = []

    for cnt in range(cnt_generate_user):
        generator: Iterator[dict] = generate_users(first_names_split, last_names_split, cities_split)
        generated_users.append(generator)

    print(generated_users)

    return None
