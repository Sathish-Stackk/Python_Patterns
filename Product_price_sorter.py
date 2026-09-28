products = {
    "Laptop": 55000,
    "Mouse": 800,
    "Keyboard": 1500,
    "Monitor": 12000
}

sorted_products = sorted(products.items(), key=lambda x: x[1])

for name, price in sorted_products:
    print(name, "₹" + str(price))
