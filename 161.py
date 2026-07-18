# Storing and fetching product prices
price_table = {
    "Laptop": 56000,
    "Keyboard": 1000,
    "Mouse": 350,
    "Monitor": 14000
}

product = input("Enter product name (Laptop/Keyboard/Mouse/Monitor): ")
if product in price_table:
    print(f"Price of {product} is: {price_table[product]} BDT")
else:
    print("Product out of stock or unavailable.")


