import random
number = random.randint(1, 100)
# print(number)

user_number = None
count = 0
levels = {1: 10, 2: 5, 3: 3}
level = int(input('Выберети уровень сложности игры: '))
max_count = levels[level]

while number != user_number:
    count += 1
    if count > max_count:
        print('Количество попыток исчерпано. Вы проиграли')
        break
    print(f'Попытка № {count}')
    user_number = int(input('Задача игры: угадать число.'
                            'Пожалуйста, введите целое число от 1 до 100: '))

    if number < user_number:
        print('К сжалению, Вы не угадали. Ваше число больше загаданного')
    elif number > user_number:
        print('К сжалению, Вы не угадали. Ваше число меньше загаданного')

    else:
        print('Победа! Вы угадали!')
