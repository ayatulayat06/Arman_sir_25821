# Finding LCM using GCD
a= int(input("Enter first number: "))
b= int(input("Enter second number: "))


m,n = a, b
while n != 0:
    m, n = n, m % n
gcd = m


lcm = (a * b) // gcd
print("LCM of", a, "and", b, "is:", lcm)

    