"""
7. В одномерном массиве целых чисел определить два наименьших элемента.
   Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint

arr = [randint(1, 20) for i in range(10)]
print(arr)

if arr[0] > arr[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0

for i in range(2, len(arr)):
    if arr[i] < arr[min1]:
        b = min1
        min1 = i
        if arr[b] < arr[min2]:
            min2 = b
    elif arr[i] < arr[min2]:
        min2 = i

print(f' элемент №{min1 + 1} : {arr[min1]}')
print(f' элемент №{min2 + 1} : {arr[min2]}')
