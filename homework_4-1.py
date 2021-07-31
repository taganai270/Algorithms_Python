"""
1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в
   рамках практического задания первых трех уроков.
"""
#  Выбрано задание №2 из урока №2.
#  Посчитать четные и нечетные цифры введенного натурального числа.
#  Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

import random
import timeit

number = int(random.random() * pow(10, 10))
print('Число:', number)


def version_1():
    count_even = 0
    count_odd = 0
    for digit in str(number):
        if int(digit) % 2 == 0:
            count_even += 1
        else:
            count_odd += 1
    print(f'Четных {count_even}\nНечетных:{count_odd}')


def version_2(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        n = num % 10
        num = num // 10
        if n % 2 == 0:
            even += 1
            return version_2(num, even, odd)
        else:
            odd += 1
            return version_2(num, even, odd)


version_1()
print(version_2(number))

time_meth_1 = timeit.timeit("version_1", setup="from __main__ import version_1")
time_meth_2 = timeit.timeit("version_2(number)", setup="from __main__ import version_2, number")

print('\nЗатраченное время на исполнение с помощью'
      f'\n{"- цикла:":25} {time_meth_1}'
      f'\n{"- рекурсии:":25} {time_meth_2}')
