"""
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на
   экран. Например, если введено число 3486, то надо вывести число 6843.
"""

num = int(input('Введите натуральное число :'))
var = 0
while num > 0:
    var = var * 10 + num % 10
    num = num // 10
print(var)
