# Printing first N Fibonacci numbers
N = int(input("Enter number of terms (N): "))
a, b = 0, 1
print("Fibonacci Series:")
for i in range(N):
    print(a)
    a, b = b, a + b

