

import csv

# Данные для записи в файл
data = [
    ["date", "branch", "product", "qty", "price"],
    ["2026-09-05", "Центр", "Латте", "40", "1200"],
    ["2026-09-05", "Центр", "Круассан", "25", "900"],
    ["2026-09-12", "Север", "Латте", "30", "1200"],
    ["2026-09-12", "Север", "Чизкейк", "15", "1500"],
    ["2026-09-20", "Центр", "Капучино", "35", "1100"],
    ["2026-09-25", "Север", "Капучино", "28", "1100"],
    ["2026-09-28", "Центр", "Чизкейк", "20", "1500"],
    ["2026-09-29", "Север", "Круассан", "22", "900"],
    ["2026-10-03", "Центр", "Латте", "22", "1200"],
    ["2026-10-07", "Центр", "Круассан", "12", "900"],
    ["2026-10-10", "Север", "Латте", "31", "1200"],
    ["2026-10-15", "Север", "Чизкейк", "6", "1500"],
    ["2026-10-18", "Центр", "Капучино", "20", "1100"],
    ["2026-10-22", "Север", "Капучино", "29", "1100"],
    ["2026-10-25", "Центр", "Чизкейк", "8", "1500"],
    ["2026-10-28", "Север", "Круассан", "21", "900"],
]

# Запись данных в файл sales.csv
with open("sales.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(data)

print("Файл sales.csv успешно создан!")

import csv

with open("sales.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
sep_revenue = sum(int(row['qty']) * int(row['price']) for row in rows if row['date'].startswith('2026-09'))
oct_revenue = sum(int(row['qty']) * int(row['price']) for row in rows if row['date'].startswith('2026-10'))

print(sep_revenue)
print(oct_revenue)



def revenue(rows, month, branch):
    total = 0
    for row in rows:
        if branch and row['branch'] != branch:
            continue
        if month and not row['date'].startswith(month):
            continue
        total += int(row['qty']) * int(row['price'])
    return total

branches = ['Центр', 'Север']
months = {'Сентябрь': '2026-09', 'Октябрь': '2026-10'}
branch_results = {}

for branch in branches:
    branch_results[branch] = {}
    for m_name, m_code in months.items():
        rev = revenue(rows, m_code, branch)
        branch_results[branch][m_code] = rev
        print(f"{branch} {m_name}: {rev}")

for branch in branches:
    rev_sep = branch_results[branch]['2026-09']
    rev_oct = branch_results[branch]['2026-10']

    if rev_sep > 0:
        pct_change = ((rev_oct - rev_sep) / rev_sep) * 100
        print(f"{branch}: {pct_change:+.2f}%")


# В октябре общая выручка кофейни упала на 32,2% (с 248 100 до 168 200 тенге), причем 85% этого спада сформировал филиал «Центр»,
# где выручка снизилась во всех категориях на 43–60%. В филиале «Север» падение составило всего 11,1%, и оно полностью обусловлено
# сокращением продаж чизкейка на 60%, аналогично просевшего и в центре. Вероятной причиной падения в филиале «Центр» могли стать
# проблемы с качеством сервиса или отток клиентов к новому конкуренту поблизости, а падение по чизкейкам связано
# с ухудшением рецептуры или сбоем поставок у поставщика.



