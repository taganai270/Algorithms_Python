"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
   случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы
"""

from random import randint

arr_rand = [randint(0, 50) for i in range(0, 10)]
print('Сгенерированный массив: ', *arr_rand)


def merge_arr(l, r):
    lst = []
    i = j = 0
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            lst.append(l[i])
            i += 1
        else:
            lst.append(r[j])
            j += 1
    if i < len(l):
        lst += l[i:]
    if j < len(r):
        lst += r[j:]
    return lst


def merge_sort(arr):
    if len(arr) == 1:
        return arr
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])
    return merge_arr(left, right)


print('Отсортированный массив: ', *merge_sort(arr_rand))
