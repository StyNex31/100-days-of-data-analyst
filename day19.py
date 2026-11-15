# cd Desktop
# mkdir dirty_data_project
# cd dirty_data_project
# mkdir src, tests, data
# Set-Content -Path README.md -Value "# Генератор грязных данных для тренировки очистки"
# Set-Content -Path .gitignore -Value "data/`n__pycache__/"
# Get-ChildItem

import csv
import os
import random
from datetime import datetime, timedelta

os.makedirs("data", exist_ok=True)

file_path = "data/sales_raw.csv"

#  список товаров
products = ["Ноутбук", "Мышь", "Клавиатура", "Монитор", "Наушники"]
start_date = datetime(2026, 1, 1)

rows = []

for i in range(1, 44):
    order_id = 1000 + i
    date_str = (start_date + timedelta(days=random.randint(0, 100))).strftime(
        "%Y-%m-%d"
    )
    product = random.choice(products)
    qty = random.randint(1, 5)
    price = round(random.uniform(500.0, 50000.0), 2)
    rows.append([order_id, date_str, product, qty, price])

for i in range(2):
    rows.append(
        [
            2000 + i,
            "2026-04-10",
            random.choice(products),
            random.randint(1, 3),
            "",
        ]
    )

rows.append([3001, "2026-03-15", "Мышь", -2, 1500.0])

rows.append([3002, "05.10.2026", "Клавиатура", 1, 3500.0])

for _ in range(3):
    rows.append(random.choice(rows))

# ии посоветовал для реализма
random.shuffle(rows)

header = ["order_id", "date", "product", "qty", "price"]

with open(file_path, mode="w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(
    f"Успешно! Создан файл '{file_path}' с 50 строками данных и внедренными аномалиями."
)