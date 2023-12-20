import os


def main():
    try:
        choice = int(input('Для входа выберите - 1,\nДля регистрации - 2,\nДля выхода  - 3\n'))
        if choice == 1:
            login()
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


def login():
    log = input('Введите имя: ')
    with open('Base.txt', 'r', encoding='utf-8') as verify:
        size = os.path.getsize('Base.txt')
        if size == 0:
            print('Необходима регистрация!')
            registration()
        else:
            for i in verify.readlines():
                user = i.split(' ')
                if log == user[0]:
                    pas = input('Введите пароль: ')
                    if pas == user[1]:
                        print(f'Wellcome, {user[0]}')
                        exit()
                    else:
                        print('Пара логин/ пароль не совпадает! \n')
                        login()
            print('Необходима регистрация!')
            registration()


def registration():
    user_reg = []
    log = input('Введите имя: ')
    with open('Base.txt', 'r', encoding='utf-8') as base:
        for i in base.readlines():
            user = i.split(' ')
            if log == user[0]:
                print('Такое имя занято! Введите другое! \n')
                registration()
            else:
                continue
    if 3 < len(log) < 20:
        user_reg.append(log)
    else:
        print('Логин должен быть больше 3 но меньше 20 символов! Повторите ввод! \n')
        registration()
    pas = input('Введите пароль: ')
    if 4 < len(pas) < 32:
        user_reg.append(pas)
    else:
        print('Пароль должен быть больше 4 но меньше 32 символов! Повторите ввод! \n')
        registration()
    data = ' '.join(user_reg)
    with open('Base.txt', 'a', encoding='utf-8') as base:
        base.write(f'{data} \n')
    main()


if __name__ == '__main__':
    main()
