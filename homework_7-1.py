"""
1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив, заданный
   случайными числами на промежутке [-100; 100). Выведите на экран исходный и
   отсортированный массивы. Сортировка должна быть реализована в виде функции. По
   возможности доработайте алгоритм (сделайте его умнее).
"""

from random import randint

arr_rand = [randint(-100, 100) for i in range(0, 10)]
print('Сгенерированный массив: ', *arr_rand)


def bubble_sort_descend(arr):
    length = len(arr)
    for el in range(length - 1):
        for i in range(length - 1 - el):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


print('Отсортированный массив: ', *bubble_sort_descend(arr_rand))
