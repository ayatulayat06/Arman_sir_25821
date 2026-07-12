# Chaking Strong Number
import math
num= int(input("Enter a number: "))
temp= num
total_sum= 0


while temp>0:
    digit= temp % 10
    total_sum += math.factorial(digit)
    temp=temp// 10


if total_sum== num:
    print(num, "is a strong number")
else:
    print(num, "is NOT a strong number")

