import re

reg_name = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_surname = re.compile(r'^[A-Za-zА-Яа-яЁё]+$')
reg_phone = re.compile(r'^[+]\d{1,3}\(\d{1,3}\)(\d{7})$')
reg_email = re.compile(r'^[A-Za-z0-9_]+@yandex\.ru$')

user_name = input("Введите имя пользователя: ")
if bool(reg_name.match(user_name)) is True:
    print("Имя принято!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")