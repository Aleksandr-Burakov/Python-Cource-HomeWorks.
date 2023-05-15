"""
Задание 4.

Запросите у пользователя значения выручки и издержек фирмы.
Определите, с каким финансовым результатом работает фирма
(прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью,
вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите
прибыль фирмы в расчете на одного сотрудника.

Пример:
Введите выручку фирмы: 1000
Введите издержки фирмы: 500
Финансовый результат - прибыль. Ее величина: 500
Значит вычисляем рентабельность выручки (соотношение прибыли к выручке)
Рентабельность выручки = 0.5
Введите численность сотрудников фирмы: 10
Прибыль фирмы в расчете на одного сотрудника = 50.0
"""

all_profit = int(input("Введите выручку фирмы :"))
if all_profit <= 0:
    print(f"Фирма работает в убыток")
if all_profit > 0:
    cost = int(input("Введите издержки фирмы :"))
    if cost > all_profit:
        print(f"Фирма работает в убыток — издержки больше выручки.")
    elif cost == all_profit:
        print(f"Согласно полученых данных, у фирмы отсутствует прибыль.")
    else:
        profit = int(all_profit) - int(cost)
        print(f"Финансовый результат фирмы - Прибыль = {profit} у.е")
        profit = int(all_profit) - int(cost)
        print(f"Финансовый результат фирмы - Прибыль = {profit} у.е")
        print(f"Cоотношение прибыли к выручке - Рентабельность выручки = \
{round((int(profit) / int(all_profit) % 100), 2)}%")
        workers = int(input("Введите численность сотрудников фирмы :"))
        print(f"Прибыль фирмы в расчете на одного сотрудника = {round((profit / workers), 2)} у.е")
