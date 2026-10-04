import os
from pathlib import Path

ENV_FILE = Path(__file__).with_name(".env")

if ENV_FILE.exists():
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            name, separator, value = line.partition("=")
            if separator:
                os.environ.setdefault(name.strip(), value.strip())

userlogin = os.getenv("APP_LOGIN")
user_password = os.getenv("APP_PASSWORD")
user_pin = os.getenv("APP_PIN")

if not userlogin or not user_password or not user_pin:
    raise SystemExit("Не найдены данные для входа. Создай .env по образцу .env.example.")

max_attempts = 3
attempts_left = max_attempts
menu_logo = "////////////"

while attempts_left > 0:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    pincode = input("Введите PIN-код: ")

    if login == userlogin and password == user_password and pincode == user_pin:
        while True:
            print(menu_logo)
            print("1 - Калькулятор")
            print("2 - Счёт от 1 до 10")
            print("3 - Выход")
            function = input("Введите одну из функций: ")

            if function == "1":
                num1_text = input("Введите первое число: ")
                num2_text = input("Введите второе число: ")

                if num1_text.strip() == "" or num2_text.strip() == "":
                    print("Введите число!")
                    continue

                try:
                    num1 = float(num1_text)
                    num2 = float(num2_text)
                except ValueError:
                    print("Нужно ввести числа, а не текст.")
                else:
                    print("Сложение:", num1 + num2)
                    print("Вычитание:", num1 - num2)
                    print("Умножение:", num1 * num2)

                    if num2 == 0:
                        print("Делить на 0 нельзя!")
                    else:
                        print("Деление:", num1 / num2)

            elif function == "2":
                for number in range(1, 11):
                    print(number)

            elif function == "3":
                print("До встречи", login, end="!")
                break

            else:
                print("Выберите 1, 2 или 3.")

        break

    else:
        attempts_left -= 1
        print("Неверно, у вас осталось", attempts_left, "попытки.")

        if attempts_left == 0:
            print("Вход не удался!")