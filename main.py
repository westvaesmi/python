import hashlib
import hmac
import json
import secrets
from pathlib import Path

HASH_ITERATIONS = 600_000
AUTH_FILE = Path(__file__).with_name(".auth.json")


def hash_credential(value, salt):
    value_bytes = value.encode("utf-8")
    return hashlib.pbkdf2_hmac("sha256", value_bytes, salt, HASH_ITERATIONS).hex()


def create_credential_record(value):
    salt = secrets.token_bytes(16)
    return {
        "salt": salt.hex(),
        "hash": hash_credential(value, salt),
    }


def credential_matches(value, saved_record):
    salt = bytes.fromhex(saved_record["salt"])
    value_hash = hash_credential(value, salt)
    return hmac.compare_digest(value_hash, saved_record["hash"])


if AUTH_FILE.exists():
    with AUTH_FILE.open("r", encoding="utf-8") as auth_file:
        saved_credentials = json.load(auth_file)
else:
    print("Первый запуск: создай данные для входа.")
    saved_credentials = {
        "login": create_credential_record(input("Придумай логин: ").strip()),
        "password": create_credential_record(input("Придумай пароль: ")),
        "pin": create_credential_record(input("Придумай PIN-код: ")),
    }
    with AUTH_FILE.open("w", encoding="utf-8") as auth_file:
        json.dump(saved_credentials, auth_file, indent=2)
    print("Данные сохранены в виде хешей.")

max_attempts = 3
attempts_left = max_attempts
menu_logo = "////////////"

while attempts_left > 0:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    pincode = input("Введите PIN-код: ")

    login_is_correct = credential_matches(login, saved_credentials["login"])
    password_is_correct = credential_matches(password, saved_credentials["password"])
    pin_is_correct = credential_matches(pincode, saved_credentials["pin"])

    if login_is_correct and password_is_correct and pin_is_correct:
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