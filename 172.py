# Function to find factorial of a number
def get_factorial(n):
    if n < 0:
        return "Invalid input"
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact
print("Factorial of 6 is:", get_factorial(6))

