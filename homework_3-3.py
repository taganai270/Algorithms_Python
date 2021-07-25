"""
3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
"""

from random import randint

arr = [randint(1, 100) for i in range(0, 10)]
print(arr)
arr.sort()
arr[0], arr[9] = arr[9], arr[0]
print(arr)
