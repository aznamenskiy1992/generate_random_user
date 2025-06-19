from src.generate import generate_users


def main(cnt_generate_user):
    """Выводит сгенерированных пользователей в консоль в списке"""
    first_names = input("Введите имена пользователей через запятую").split(",")
    last_names = input("Введите фамилии пользователей через запятую").split(",")
    cities = input("Введите названия городов через запятую").split(",")

    generated_users = []

    for cnt in range(cnt_generate_user):
        generator = generate_users(first_names, last_names, cities)
        generated_users.append(generator)

    print(generated_users)

    return None
