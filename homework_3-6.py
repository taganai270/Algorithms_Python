"""
6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
   Сами минимальный и максимальный элементы в сумму не включать.
"""


from random import randint

arr = [randint(1, 20) for i in range(10)]
print(arr)


min_el = 0
max_el = 0
for i in range(1, len(arr)):
    if arr[i] < arr[min_el]:
        min_el = i 
    elif arr[i] > arr[max_el]:
        max_el = i
print(f'Минимальный элемент {arr[min_el]}\nМаксимальный элемент {arr[max_el]}')
if min_el > max_el:
    min_el, max_el = max_el, min_el
summa = 0
for i in range(min_el + 1, max_el):
    summa += arr[i]
print('Сумма -', summa)
