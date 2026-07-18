# Printing first N Factorial values
N = int(input("Enter N: "))
fact = 1
print("Factorial Series up to", N, ":")
for i in range(1, N + 1):
    fact *= i
    print(f"{i}! = {fact}")


