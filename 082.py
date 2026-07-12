# Checking Armstrong number
n = int(input("Enter a number: "))

num_digits = str(n)
poewer= len(num_digits)
total_sum = 0

temp= n
while temp > 0:
    digit = temp % 10
    total_sum += digit ** poewer
    temp //= 10

if total_sum == n:
    print(n, "is an Armstrong number.")
else:
    print(n, "is not an Armstrong number.")
    