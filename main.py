user_login = 'login'
user_password = 'log'
user_pin = '1554'
max_attempts = 3
attempts_left = max_attempts
menu_logo = '////////////'

while attempts_left > 0:
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    pincode = input("Введите PIN-код: ")

    if login == user_login and password == user_password and pincode == user_pin:
        while True:
            print(menu_logo)
            print("1 - Калькулятор")
            print("2 - Счёт от 1 до 10")
            print("3 - Выход")
            function = input("Введите одну из функций: ")

            if function == '1':
                num1_text = input("Введите первое число: ")
                num2_text = input('Введите второе число: ')

                if num1_text.strip() == '' or num2_text.strip() == '':
                    print("Введите число!")
                    continue

                try:
                    num1 = float(num1_text)
                    num2 = float(num2_text)
                except ValueError:
                    print("Вам нужно написать цифру!")
                else:
                    print("Добавление: ", num1 + num2)
                    print("Вычитание: ", num1 - num2)
                    print("Умножение: ", num1 * num2)

                    if num2 == 0:
                        print("Делить на 0 нельзя!")
                    else:
                        print("Деление: ", num1 / num2)

            elif function == '2':
                for i in range(1, 11):
                    print(i)
            elif function == '3':
                print('До встречи', login, end="!")
                break
            else:
                print('Выберите 1, 2 или 3.')

        break

    else:
        attempts_left -= 1
        print("Неверно, у вас осталось", attempts_left, end=' Попытки!\n')

        if attempts_left == 0:
            print("Вход не удался!")
            break