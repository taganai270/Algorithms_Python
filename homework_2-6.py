"""
6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его
   отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться
   больше или меньше введенное пользователем число, чем то, что загадано. Если за 10
   попыток число не отгадано, то вывести загаданное число.
"""
import random

answer = random.randint(0, 100)
counter = 1
print('Угадай число от 0 до 100 за десять попыток')

while counter <= 10:
    user_answer = int(input('Введи число :'))
    if user_answer == answer:
        print(f'Вы угадали, это число {answer}.')
        break
    if user_answer < answer:
        print('Загаданное число больше. Попробуй ещё :')
    else:
        print('Загаданное число меньше. Попробуй ещё :')
    counter += 1

else:
    print(f'Вы не угадали. Загаданное число - {answer}')
