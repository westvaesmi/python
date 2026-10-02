user_login = 'Banger'
user_password = 'Ma4'
user_pincode = '1654'
again = 3
menu_default = '////////////'

while again > 0:
    login = input("Введите ваш логин: ")
    password = input('Введите ваш пароль:')
    pin_code = input("Введите ваш пин-код:")

    if login == user_login and password == user_password and pin_code == user_pincode:

        start_menu = True
        while start_menu:
            print(menu_default)
            print("Добро пожаловать ", login, end='!')
            print(menu_default)
            print("1 - Калькулятор")
            print("2 - Счёт от 1 до 10")
            print("3 - Выход")

            function = input("Введите одну из функций: ")

            if function == '1':
                num1 = int(input("Введите первое число: "))
                num2 = int(input("Введите второе число: "))

                print("Добавление: ",num1 + num2)
                print("Вычитывание: ",num1 - num2)
                print("Умножение:",num1 * num2)
                print("Деление: ", num1 / num2)
            elif function == '2':
                for i in range(11):
                    print(i)
            elif function == '3':
                print("До встречи", login, end="!")
                quit()
            else:
                print("Error")







    else:
        again -= 1
        print("Неверно , у вас осталось",again, end=' Попытки!\n')

        if again == 0:
            print("Лимит исчерпан!")