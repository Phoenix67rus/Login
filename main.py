import os

def start():
    try:
        choice = int(input('Для входа выберите - 1,\n для регистрации - 2,\n для выхода  - 3\n '))
        if choice == 1:
            login()
        elif choice == 2:
            registr()
        elif choice == 3:
            exit()
        else:
            print('Введенное число должно быть от 1 до 3!')
            start()
    except ValueError:
        print('Вы ввели буквы, а надо цифры!')
        start()

def login():
    log = input('Введите имя: ')
    pas = input('Введите пароль: ')
    with open('Base.txt', 'r', encoding='utf-8') as login:
        size = os.path.getsize('Base.txt')
        if size == 0:
            print('Необходима регистрация!')
            start()
        else:
            for i in login.readlines():
                user = i.split(' ')
                if log == user[0] and pas == user[1]:
                    print(f'Wellcome, {user[0]}')
                    exit()
                else:
                    print('Необходима регистрация!')
                    start()


def registr():
    user = []
    log = input('Введите имя: ')
    if 3 < len(log) < 20:
        user.append(log)
    else:
        print('Логин должен быть больше 3 но меньше 20 символов! Повторите ввод!')
        registr()
    pas = input('Введите пароль: ')
    if 4 < len(pas) < 32:
        user.append(pas)
    else:
        print('Пароль должен быть больше 4 но меньше 32 символов! Повторите ввод!')
        registr()
    data = ' '.join(user)
    with open('Base.txt', 'w', encoding='utf-8') as login:
        login.write(data)


def main():
    start()


if __name__ == '__main__':
    main()