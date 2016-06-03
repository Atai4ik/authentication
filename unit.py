# Задача 1.

# Написать unıttests на алгоритмы:

# * сортировки по возрастанию/убыванию

# * нахождению максимального/минимального значения



# TODO:

# 1. Создать папку algorithms/

# 2. Создать два файла: tests.py, script.py

# 3. Перенести алгоритмы в файл script.py

# 4. Импортировать алгоритмы в файл тестов tests.py

# 5. Описать тесты

# 6. Опубликовать репозиторий на гитхаб



# Задача 2.

# Создать класс User

# Указать параметры:

# * login - <string> латиница, от 6 символов

# * password - <string> латиница, от 8 символов

# * first_name - <string> кириллица/латиница, от 2 символов

# * last_name - <string> кириллица/латиница, от 2 символов

# * is_active - <boolean> True/False

# Указать методы

# * def sıgnın(login, password) - Регистрация пользователя

# * def reset_password(login) - Сбросить пароль, выводит новый пароль

# * def is_active() - Проверяем активен ли пользователь

# * def change_profile_detail(first_name, last_name) - Указываем имя, фамилию пользователя

# * def check_password(unverified_password) - Проверяем пароль



# * def send_confirmation_password() - Отправка письма пользователю

import hashlib



def signin(self, login, password=None):
    if len(login) > 6:
        self.login = login
    if len(password) > 8:
        self.password = password
    elif password is None:
        self.password = hashlib.md5(self.login)[:8]
        self.is_active = True
    return (self.login, self.password, self.is_active)
