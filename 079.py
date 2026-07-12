 # Finding GCD using Euclidean algorithm
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

m, n = a, b
while n != 0:
    m, n = n, m % n
print("The GCD of: ", a, "and", b, "is:", m)
