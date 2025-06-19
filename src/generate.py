import random


def generate_users(first_names, last_names, cities):
    """Генерирует случайного пользователя из полученных данных и возвращает его в словаре"""
    invalid_args = [name for name, arg in zip(
        ['first_names', 'last_names', 'cities'],
        [first_names, last_names, cities]
    ) if not isinstance(arg, list)]

    if invalid_args:
        raise TypeError(f"Аргументы должны быть переданы в списках. Не в списках: {", ".join(invalid_args)}")

    while True:
        generated_user = {
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "age": random.randint(18, 65),
            "city": random.choice(cities)
        }
        yield generated_user
