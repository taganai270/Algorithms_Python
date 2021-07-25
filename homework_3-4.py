"""
4. Определить, какое число в массиве встречается чаще всего.
"""


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
