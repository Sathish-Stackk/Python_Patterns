prices = [499, 799, 299, 999]
quantities = [2, 1, 3, 1]

total = sum(price * quantity for price, quantity in zip(prices, quantities))

print("Total Items:", sum(quantities))
print("Cart Total: ₹", total)
print("Average Item Price: ₹", round(total / sum(quantities), 2))
