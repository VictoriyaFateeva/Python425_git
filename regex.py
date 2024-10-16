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

user_last_name = input("Введите фамилию пользователя: ")
if bool(reg_surname.match(user_last_name)) is True:
    print("Фамилия принята!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

user_phone = input("Введите телефон пользователя: ")
if bool(reg_phone.match(user_phone)) is True:
    print("Телефон принят!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

user_mail = input("Введите email пользователя на яндексе: ")
if bool(reg_email.match(user_mail)) is True:
    print("email принят!")
else:
    print("Ввод некорректен! Повторите ввод данных!\n")

print("Хочу создать конфликт!")

print("Хочу решить конфликт!")

print("Хочу пушить в сразу в прод!")

print("Это мой первый pull-request")
print("Это моя доработка")

print("Были доработки от других разработчиков")
print("Код для конфликта")

print("Код для разрешения конфликта!")
print("Код для выделенной ветки!")

print('новое')
