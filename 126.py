# Separating even numbers from list
numbers = [12, 15, 18, 21, 24, 27, 30]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)
print("Original list:", numbers)
print("Even numbers:", evens)

