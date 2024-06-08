"""
Модуль для работы с файлом, содержащим данные пользователей.

Этот модуль предоставляет класс FileWorker с методами для создания, чтения и
записи файла, содержащего логины и пароли пользователей.

Классы:
    FileWorker: Класс для работы с файлом пользователей.

Константы:
    BASE_FILE: Имя файла, в котором хранятся данные пользователей.
"""
from typing import Union

BASE_FILE = 'Base.txt'


class FileWorker:
    @staticmethod
    def create_file() -> None:
        """
        Функция открывает файл для добавления данных.
        Создает файл если он не существует
        """
        with open(BASE_FILE, 'a'):
            pass

    @staticmethod
    def read_file() -> list:
        """
        Считывает данные из файла.

        Осуществляет чтение данных из файла с логином и паролем.

        Returns:
            list: Список строк, считанных из файла.
        """
        with open(BASE_FILE, 'r') as file:
            return file.readlines()

    @staticmethod
    def write_file(login: Union[str, int], password: Union[str, int]):
        """
        Записывает данные в файл.

        Осуществляет добавление логина и пароля в файл.

        Args:
            login (Union[str, int]): Логин пользователя.
            password (Union[str, int]): Пароль пользователя.
        """
        with open(BASE_FILE, 'a') as file:
            file.write(f'{login} {password} \n')
