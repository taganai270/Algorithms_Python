"""
4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
   Количество элементов (n) вводится с клавиатуры.
"""

quantity = int(input('Введите количество элементов :'))
n = [1]
sum_n = el = 0
while quantity > 1:
    n.append(n[el] / -2)
    el += 1
    quantity -= 1
for i in n:
    sum_n = sum_n + i

print(f'Сумма элементов {n} = {sum_n} ')
