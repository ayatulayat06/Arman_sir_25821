# Separating negative numbers
numbers = [-15, 20, -8, 35, -2, 50, 0]
negatives = []
for num in numbers:
    if num < 0:
        negatives.append(num)
print("Negative numbers:", negatives)


