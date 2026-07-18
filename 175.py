# Function to find maximum among arbitrary numbers using *args
def find_max(*numbers):
    if not numbers:
        return None
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
print("Max among (10, 50, 25):", find_max(10, 50, 25))
print("Max among (5, 99, 12, 105, 88):", find_max(5, 99, 12, 105, 88))