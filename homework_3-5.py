"""
5. В массиве найти максимальный отрицательный элемент.
   Вывести на экран его значение и позицию в массиве.
"""


from random import randint

arr = [randint(-10, -1) for i in range(10)]
print(arr)

i = 0
index = -1
while i < len(arr):
    if arr[i] < 0 and index == -1:
        index = i
    elif 0 > arr[i] > arr[index]:
        index = i
    i += 1
 
print(f'Индекс элемента {index} : элемент {arr[index]}')
