"""
1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""


num = input('Введите трёхзначное число :')
print(f'Сумма первых трёх чисел равна : {int(num[0]) + int(num[1]) + int(num[2])}')
print(f'Произведение первых трёх чисел равно : {int(num[0]) * int(num[1]) * int(num[2])}')
