
city_almaty = {"name": "Алматы", "population": 2000000}
city_astana = {"name": "Астана", "population": 1200000}
city_taldyqorgan = {"name": "Талдыкорган", "population": 300000}

cities_ry = [city_almaty, city_astana, city_taldyqorgan]

print(cities_ry)

def total_expenses(cities_ry):
    total = 0
    for city in cities_ry:
        total += city['population']
    return total
print(total_expenses(cities_ry))
