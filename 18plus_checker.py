#!/usr/bin/env python3

age = int(input('Введите свой возраст: '))

# Если возраст меньше 18 лет
# выводим на экран "Доступ запрещен"
if age < 18:
    print('Доступ запрещен')

# Иначе - выводим на экран "Доступ разрешен"
else:
    print('Доступ разрешен')

print('Дальнейшие действия')
print('end')

# Примеры

# Введите свой возраст: 30
# Доступ разрешен
# Дальнейшие действия
# end

# Введите свой возраст: 6
# Доступ запрещен
# Дальнейшие действия
# end