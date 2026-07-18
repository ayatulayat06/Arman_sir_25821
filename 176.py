# Function to find sum of list elements
def sum_list(my_list):
    total = 0
    for num in my_list:
        total += num
    return total
sample_list = [10, 20, 30, 40, 50]

print("Sum of list elements:", sum_list(sample_list))

