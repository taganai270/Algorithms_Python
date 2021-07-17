"""
8. Определить, является ли год, который ввел пользователем,
    високосным или не високосным.
"""


year = input('Введите год ')
year = year[:4]
if year.isdigit():
    year = int(year)
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, '- високосный год')
    else:
        print(year, '- не високосный год')
else:
    print('Неверный ввод')


           