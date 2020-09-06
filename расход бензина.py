""" Расход бензина по количеству километров
    Цена за одну поездку, за месяц на 92ой и 95ый
"""

consumption_per_km = float(input("Расход: ")) / 100
distance = int(input("Расстояние: "))
price92 = float(input("Цена 92: "))
price95 = float(input("Цена 95: "))
cost92 = (consumption_per_km * distance) * price92
cost95 = (consumption_per_km * distance) * price95
print(f"Цена за поездку на 92ом бензине: {cost92}, \nцена за 30 дней туда/обратно: {(cost92 * 30) * 2}")
print(f"Цена за поездку на 95ом бензине: {cost95}, \nцена за 30 дней туда/обратно: {(cost95 * 30) * 2}")
