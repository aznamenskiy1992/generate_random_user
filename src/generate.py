import random


def generate_users(first_names, last_names, cities):
    """Генерирует случайного пользователя из полученных данных и возвращает его в словаре"""
    args_with_incorrect_type = []
    args = {
        "first_names": first_names,
        "last_names": last_names,
        "cities": cities,
    }

    for key, value in args.items():
        if not isinstance(value, list):
            args_with_incorrect_type.append(key)

    if len(args_with_incorrect_type) > 0:
        raise TypeError(f"Аргументы должны быть переданы в списках. Не в списках: {", ".join(args_with_incorrect_type)}")

    while True:
        generated_user = {
            "first_name": random.choice(first_names),
            "last_name": random.choice(last_names),
            "age": random.randint(18, 65),
            "city": random.choice(cities)
        }
        yield generated_user
