import os


def authorization():
    login = input('Введите имя: ')
    try:
        with open('Base.txt', 'r', encoding='utf-8') as verify:
            size = os.path.getsize('Base.txt')
            if size == 0:
                print('Необходима регистрация!')
                registration()
            else:
                for i in verify.readlines():
                    user = i.split(' ')
                    if login == user[0]:
                        password = input('Введите пароль: ')
                        if password == user[1]:
                            print(f'Wellcome, {user[0]}')
                            exit()
                        else:
                            print('Пара логин/ пароль не совпадает! \n')
                            authorization()
                print('Необходима регистрация!')
                registration()
    except FileNotFoundError:
        with open('Base.txt', 'a', encoding='utf-8'):
            pass
        authorization()


def registration():
    login = input('Введите имя: ')
    with open('Base.txt', 'r', encoding='utf-8') as base:
        for i in base.readlines():
            user = i.split(' ')
            if login == user[0]:
                print('Такое имя занято! Введите другое! \n')
                registration()
            else:
                continue
    if not len(login) in range(3, 21):
        print('Логин должен быть больше 3 но меньше 20 символов! Повторите ввод! \n')
        registration()
    password = input('Введите пароль: ')
    if not len(password) in range(4, 33):
        print('Пароль должен быть больше 4 но меньше 32 символов! Повторите ввод! \n')
        registration()
    with open('Base.txt', 'a', encoding='utf-8') as base:
        base.write(f'{login} {password} \n')
    main()


def main():
    try:
        choice = int(input('Для входа выберите - 1,\nДля регистрации - 2,\nДля выхода  - 3\n'))
        if choice == 1:
            authorization()
        elif choice == 2:
            registration()
        elif choice == 3:
            exit()
        else:
            print('Введенное число должно быть от 1 до 3!')
            main()
    except ValueError:
        print('Вы ввели буквы, а надо цифры!')
        main()


if __name__ == '__main__':
    main()