"""
CP1404 - Prac01 - Shop Calculator
Date: 02/02/2024
Author: Nathaniel Carl Peter
"""

"""
Pseudo:

total = 0
get number of items
for i in number items
    get price
    total = total + price
if total > 100
    total = total * 0.1
display total price
"""

DISCOUNT = 0.9  # 10%
total_cost = 0

number_of_items = int(input("Number of items: "))
for item in range(number_of_items):
    item_cost = float(input("Price of item: "))
    total_cost += item_cost
if total_cost > 100:
    total_cost *= DISCOUNT
print(f"Total price of {number_of_items} items is ${total_cost:.2f}")

