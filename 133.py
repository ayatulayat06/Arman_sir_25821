# Searching an element in a list (Linear Search)
numbers = [15, 28, 35, 42, 59, 64]
target = int(input("Enter number to search: "))
found = False
for i in range(len(numbers)):
    if numbers[i] == target:
        print(f"Number {target} found at index {i}")
    found = True
    break
if not found:
    print(f"Number {target} is NOT in the list")

    