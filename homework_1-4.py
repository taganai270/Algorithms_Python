"""
4. Написать программу, которая генерирует в указанных пользователем границах
    ● случайное целое число,
    ● случайное вещественное число,
    ● случайный символ.
    Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если
    надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна
    вывести на экран любой символ алфавита от 'a' до 'f' включительно.

"""
import random

start, end = map(str, input('Введите границы диапазона генерируемых символов,'
                            ' например (100 200) или (a z) ').split())
try:
    if start.isdigit() and end.isdigit():
        start, end = int(start), int(end)
        print(f'Случайное целое число в диапазоне {start} - {end} :', random.randint(start, end))
        print(f'Случайное вещественное число в диапазоне {start} - {end} :',
              round((random.random() * (end - start) + start), 2))

    elif start.isalpha() and end.isalpha():
        start, end = start.lower(), end.lower()
        print(f'Случайный символ в диапазоне {start} - {end} :', chr(random.randint(ord(start), ord(end))))
except:
    print('Неверный ввод')
