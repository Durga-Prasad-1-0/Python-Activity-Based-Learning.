distance = float(input("Enter journey distance in km: "))
fuel_price = float(input("Enter fuel price per litre: "))

vehicles = [
    ("Bike", 40),
    ("Car", 15),
    ("Mileage Car", 20)
]

costs = []

if distance <= 0 or fuel_price <= 0:
    print("Enter valid distance and fuel price")
else:
    for name, mileage in vehicles:
        fuel = distance / mileage
        cost = fuel * fuel_price
        costs.append((name, cost))

        print(name)
        print("Fuel required:", round(fuel, 2), "litres")
        print("Travel cost: Rs.", round(cost, 2))

    cheapest = min(costs, key=lambda item: item[1])
    print("Cheapest vehicle:", cheapest[0])
    print("Minimum cost: Rs.", round(cheapest[1], 2))
