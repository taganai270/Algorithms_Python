"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
   в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
   одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
   Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
   используйте метод сортировки, который не рассматривался на уроках.
"""

from random import randint


def no_sort_median(arr):
    pivot = arr[0]

    less_med_el = []
    greater_med_el = []
    left_side = 0
    right_side = 0

    for i in array:
        if i < pivot:
            left_side += 1
        elif i > pivot:
            right_side += 1

        if i in arr:
            if i < pivot:
                less_med_el.append(i)
            elif i > pivot:
                greater_med_el.append(i)

    if left_side > right_side:
        return no_sort_median(less_med_el)
    elif left_side < right_side:
        return no_sort_median(greater_med_el)

    return pivot


n = int(input('Введите положительное целое число: '))
m = 2 * n + 1
print(f'Количество элементов m = 2 * {n} + 1 = {m}')

max_val = pow(m, 2)
array = []
while len(array) < m:
    x = randint(0, max_val)
    if x not in array:
        array.append(x)

print('Массив: ', *array)
print('Медиана: ', no_sort_median(array))
