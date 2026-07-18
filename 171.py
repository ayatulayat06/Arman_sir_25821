# Function to divide two numbers with Zero check
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


print("Division Result:", divide(50, 4))
print("Zero Division Test:", divide(20, 0))

