from Main import json_tel

surname = (input('Введите фамилию: '))
name = (input('Введите имя: '))
tel = (input('Введите телефон в формате 123-45-67: '))
description = (input('Введите описание: '))

json_tel[tel] = {'surname': surname, 'name': name, 'description': description}

for a, b in json_tel.items():
    print(a, b)
