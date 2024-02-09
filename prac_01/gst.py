"""
Get user item price
"""

"""
GST = 0.1

get item cost,gst
if gst == "Y"
    price = GST * item cost
else
    price = item cost
display final price
"""

GST = 0.1

item_price = float(input("Cost: $"))
item_gst = input("Does it have GST(y/n): ").upper()
if item_gst == "Y":
    price = item_price * GST
else:
    price = item_price
print(f"${price:.2f}")
