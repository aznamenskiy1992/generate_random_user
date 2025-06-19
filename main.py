from src.generate import generate_users


def main(cnt_generate_user):
    """Выводит сгенерированных пользователей в консоль в списке"""
    first_names = input("Введите имена пользователей через запятую")
    last_names = input("Введите фамилии пользователей через запятую")
    cities = input("Введите названия городов через запятую")

    if None in (first_names, last_names, cities):
        raise ValueError("Не введены параметры пользователя")

    first_names_split = first_names.split(",")
    last_names_split = last_names.split(",")
    cities_split = cities.split(",")

    generated_users = []

    for cnt in range(cnt_generate_user):
        generator = generate_users(first_names_split, last_names_split, cities_split)
        generated_users.append(generator)

    print(generated_users)

    return None
