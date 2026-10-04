user_login = "demo_user"
user_password = "demo_password"
user_pincode = "1234"

max_attempts = 3
attempts_left = max_attempts
menu_line = "////////////"

while attempts_left > 0:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    pincode = input("Введите PIN-код: ")

    if login == user_login and password == user_password and pincode == user_pincode:
        print("Вход выполнен!")

        while True:
            print(menu_line)
            print("1 — Калькулятор")
            print("2 — Счёт от 1 до 10")
            print("3 — Выход")

            choice = input("Введите номер опции: ")

            if choice == "1":
                num1_text = input("Введите первое число: ")
                num2_text = input("Введите второе число: ")

                if num1_text.strip() == "" or num2_text.strip() == "":
                    print("Ты не ввёл число!")
                else:
                    try:
                        num1 = float(num1_text)
                        num2 = float(num2_text)
                    except ValueError:
                        print("Нужно ввести числа.")
                    else:
                        print("Сложение:", num1 + num2)
                        print("Вычитание:", num1 - num2)
                        print("Умножение:", num1 * num2)

                        if num2 == 0:
                            print("Делить на 0 нельзя!")
                        else:
                            print("Деление:", num1 / num2)

            elif choice == "2":
                for number in range(1, 11):
                    print(number)

            elif choice == "3":
                print("Выход из программы. До встречи!")
                break

            else:
                print("Такой опции нет. Выбери 1, 2 или 3.")

        break

    else:
        attempts_left -= 1
        print("Неверный логин, пароль или PIN.")
        print("Осталось попыток:", attempts_left)

        if attempts_left == 0:
            print("Попытки закончились.")