# Finding minimum in a list
numbers = [45, 89, 12, 96, 54, 23]
min_val = numbers[0]
for num in numbers:
    if num < min_val:
        min_val = num
print("Minimum number is:", min_val)


