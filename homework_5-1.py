"""
1. Пользователь вводит данные о количестве предприятий,
   их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
   Программа должна определить среднюю прибыль (за год для всех предприятий)
   и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
   наименования предприятий, чья прибыль ниже среднего.
"""


import collections

n = int(input('Введите количество предприятий: '))
    
company = collections.defaultdict()
income_comp = collections.deque()
loss_comp = collections.deque()
all_profit = 0
Q = 4

for i in range(n):
    name = input(f'\nВведите название {i+1}-й компании: ')
    profit = 0
    q = 1
    while q <= Q:
        try:
            profit += float(input(f'Введите прибыль за {q}-й квартал: '))
        except ValueError:
            print('Вы ввели недопустимое значение')
            continue
        q += 1
    company[name] = profit
    all_profit += profit

mid_profit = all_profit / n
for i, item in company.items():
    if item >= mid_profit:
        income_comp.append(i)
    else:
        loss_comp.append(i)

print(f'Средняя прибыль для всех компаний составила: {mid_profit}')

print(f'Прибыль выше среднего у {len(income_comp)} компаний:')
for name in income_comp:
    print(name)

print(f'Прибыль ниже среднего у {len(loss_comp)} компаний:')
for name in loss_comp:
    print(name)
