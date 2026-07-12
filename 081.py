# Checking perfect number
n = int(input("Enter a number: "))

if n < 1:
    print("Please enter a positive integer.")
else:
    sum_divisors = 0
    for i in range(1, (n//2)+1):
        if n % i == 0:
            sum_divisors += i
    if sum_divisors == n:
        print(n, "is a perfect number.")
    else:
        print(n, "is not a perfect number.")