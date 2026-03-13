print ("Doctor chips Restaurant")

kilogram_price = float(input("state  the price charged per kilogram: "))
meal_weight = float(input("Provide the price per kilogram of the costumer´s meal: "))

meal_price = kilogram_price * kilogram_price

print (f"the price of the meal is ${meal_price: .2f}")

if meal_weight > 1:
    print("as the weigth of the meal exited 2kg, they need to pay just the fixed value of $ 8,00")

