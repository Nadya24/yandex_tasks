# Расчет P&L
# Представьте, что вашей компании требуется сформировать отчет P&L
# для расчета итоговых прибылей и убытков
#  (например, расчет прибыли за год, если известен доход за день).
# Вы решили написать программу, которая принимает
# на вход именованные аргументы с известными доходами/расходами
# (вещественные числа) в день/неделю/месяц/год (--per-day, —per-week,
# —per-month, —per-year)
# и период времени за который требуется рассчитать итоговый результат.
# Это может быть день, месяц или год (--get-by [day, month, year]).
# Других значений параметр —get-by принимать не может.

# Программа должна выводить вычисленную сумму за указанный период рассчета,
# при этом, если он явно не указан, то
#  надо рассчитывать P&L за день.

# При выводе суммы ее необходимо привести к целому числу с помощью int().
# Пример 1
# Ввод Вывод
# python3 solution.py —per-day +1 —per-week -7 —get-by month
# 0
# Пример 2
# Ввод Вывод
# python3 solution.py —per-year +360 —per-day -2
# -1
# Пример 3
# Ввод Вывод
# python3 solution.py —per-day 1 —per-week -14 —per-year 360
# —per-month 7 —get-y what
# usage: solution.py [-h] [--per-day PER_DAY] [--per-week PER_WEEK]
# [--per-month PER_MONTH] [--per-year PER_YEAR]
# [--get-by {day,month,year}]
# solution.py: error: argument —get-by: invalid choice:
# 'what' (choose from 'day', 'month', 'year')
# Примечания
# При рассчете можно полагаться на следующие аксиомы:
# 1 год = 360 дней, 1 месяц = 30 дней, 1 неделя = 7 дней.

# При решении необходимо пользоваться библиотекой argparse
#

import argparse

parser = argparse.ArgumentParser()

t = {
    'day': 1,
    'year': 360,
    'month': 30,
    'week': 7
}

parser.add_argument('--per-day', type=float)
parser.add_argument('--per-week', type=float)
parser.add_argument('--per-month', type=float)
parser.add_argument('--per-year', type=float)
parser.add_argument('--get-by', default='day',
                    choices=['day', 'month', 'year'])

args = parser.parse_args()

summa = 0
if args.per_day:
    summa = summa + args.per_day

if args.per_week:
    summa = summa + args.per_week / t['week']

if args.per_month:
    summa = summa + args.per_month / t['month']

if args.per_year:
    summa = summa + args.per_year / t['year']

print(int(summa * t[args.get_by]))
