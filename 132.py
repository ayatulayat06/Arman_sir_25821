# Removing duplicates while preserving order
numbers = [10, 25, 10, 30, 25, 40, 50, 30]
unique_list = []
for num in numbers:
    if num not in unique_list:
        unique_list.append(num)
print("Original list:", numbers)
print("Without duplicates:", unique_list)

