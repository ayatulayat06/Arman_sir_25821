a = int(input("Enter a number: "))
squere = a**2


temp = squere
sum_digits = 0
while temp >0:
    digit = temp % 10
    sum_digits += digit 
    temp = temp//10


if sum_digits == a:
    print(a, "is a neon number")


else:
    print(a, "is NOT neon number")


