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
    with open('Base.txt', 'r', encoding='utf-8') as login:
        size = os.path.getsize('Base.txt')
        if size == 0:
            print('Необходима регистрация!')
            registr()
        else:
            for i in login.readlines():
                user = i.split(' ')
                if log == user[0]:
                    pas = input('Введите пароль: ')
                    if pas == user[1]:
                        print(f'Wellcome, {user[0]}')
                        exit()
                    else:
                        print('Введен не верный пароль! \n')
                        main()
                elif log != user[0]:
                    pass
                else:
                    print('Необходима регистрация!')
                    registr()


def registr():
    userreg = []
    log = input('Введите имя: ')
    with open('Base.txt', 'r', encoding='utf-8') as login:
        for i in login.readlines():
            user = i.split(' ')
            if log == user[0]:
                print('Такое имя занято! Введите другое! \n')
                registr()
            else:
                continue
    if 3 < len(log) < 20:
        userreg.append(log)
    else:
        print('Логин должен быть больше 3 но меньше 20 символов! Повторите ввод! \n')
        registr()
    pas = input('Введите пароль: ')
    if 4 < len(pas) < 32:
        userreg.append(pas)
    else:
        print('Пароль должен быть больше 4 но меньше 32 символов! Повторите ввод! \n')
        registr()
    data = ' '.join(userreg)
    with open('Base.txt', 'a', encoding='utf-8') as login:
        login.write(f'{data} \n')
    start()

def main():
    start()


if __name__ == '__main__':
    main()