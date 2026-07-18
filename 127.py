# Separating odd numbers from list
numbers = [12, 15, 18, 21, 24, 27, 30]
odds = []
for num in numbers:
    if num % 2 != 0:
        odds.append(num)
print("Odd numbers:", odds)

