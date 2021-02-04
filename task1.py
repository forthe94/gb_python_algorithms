"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
предприятий, чья прибыль выше среднего и ниже среднего.
"""

from collections import namedtuple

Facility = namedtuple('Facility', 'name profit1 profit2 profit3 profit4 year_sum')

fac_count = int(input('Введите количество предприятий: '))
fac_tuple = []
num = 1
avg = 0
for _ in range(fac_count):

    name = input(f'Введите имя препдприятия {num}: ')
    profit1 = int(input('Введите прибыль за первый квартал: '))
    profit2 = int(input('Введите прибыль за второй квартал: '))
    profit3 = int(input('Введите прибыль за третий квартал: '))
    profit4 = int(input('Введите прибыль за четвёртый квартал: '))
    year_sum = profit1 + profit2 + profit3 + profit4
    fac_tuple.append(Facility(name, profit1, profit2, profit3, profit4, year_sum))
    avg += year_sum
    num += 1
    print()

avg /= fac_count
print(f'Средняя прибыль предприятий за год {avg}')

less_avg = [fac.name for fac in fac_tuple if fac.year_sum < avg]
more_avg = [fac.name for fac in fac_tuple if fac.year_sum >= avg]

print('Предприятия с суммой больше средней:', more_avg)
print('Предприятия с суммой меньшей средней:', less_avg)