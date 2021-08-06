"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
   Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

   Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи.
   Результаты анализа вставьте в виде комментариев к коду.
   Также укажите в комментариях версию Python и разрядность вашей ОС.
"""
# Python version 3.9.1
# OC Windows 64

import sys

# Задача: 2-2.
# Посчитать четные и нечетные цифры введенного натурального числа. Например, если
# введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).


num = input('Введите натуральное положительное число :')
even = odd = 0
if num.isdigit():
    for el in num:
        if int(el) % 2 == 0:
            even += 1
        else:
            odd += 1
    print(f'Чётных чисел - {even}\nНечётных чисел - {odd}')
else:
    print('Ошибка ввода')

sum_member = sys.getsizeof(even) + sys.getsizeof(odd) + sys.getsizeof(num)
print('В программе задействовано байт памяти: {}'.format(sum_member))

# Выполнение программы:
# Введите натуральное положительное число :2345998756734
# Чётных чисел - 5
# Нечётных чисел - 8
# В программе задействовано байт памяти: 118
#
# В данной программе затраты памяти  зависят от того, какой длинны число будет введено
# При вводе 123 результат будет: 108 байт.
# При вводе 2345678987654321 результат будет уже : 121 байт.

# -----------------------------------------------------------------------------------------------------
# Задача: 1-9
# 9.Вводятся три разных числа. Найти, какое из них является средним(больше одного, но меньше другого)

a, b, c = map(int, input('Введите три целых подожительных числа  a b c ').split())
if a > b and b > c and a > c:
    print('Среднее число b -', b)
elif b > a and a > c and b > c:
    print('Среднее число a -', a)
else:
    print('Среднее число c -', c)

sum_member = sys.getsizeof(a) + sys.getsizeof(b) + sys.getsizeof(c)
print('В программе задействовано байт памяти: {}'.format(sum_member))

# Выполнение программы:
# Введите три целых подожительных числа  a b c 234 566 12
# Среднее число a - 234
# В программе задействовано байт памяти: 84
# В данной программе затраты памяти  зависят длинны вводимых чисел.
# При вводе 234 566 12 результат будет: 84 байт.
# При вводе девятиразрядных чисел 123123123 456456456 789789789 результат будет так же : 84 байт.
# При вводе шестнадцатиразрядных чисел 12345678987654321 98765432123456789 22222222222223 результат уже : 96 байт.

# ----------------------------------------------------------------------------------------------------
# задача: 3-4
# Определить, какое число в массиве встречается чаще всего.

from random import randint

arr = [randint(1, 5) for i in range(10)]
print(arr)
num_repeat = 0
num_quantity = 0

for item in set(arr):
    num_q = arr.count(item)
    if num_q > num_quantity:
        num_quantity = num_q
        num_repeat = item

print(num_repeat)
sum_member = sys.getsizeof(arr) + sys.getsizeof(num_repeat) + sys.getsizeof(num_quantity)
print('В программе задействовано байт памяти: {}'.format(sum_member))

# Выполнение программы:
# [5, 4, 1, 4, 5, 4, 1, 3, 1, 2]
# 1
# В программе задействовано байт памяти: 240
#
# Количество памяти всегда одинаково, потому что размер массива - константа.
