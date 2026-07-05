num = int (input("Enter a number"))
temp = abs (num)
sum_digit = 0
while temp >0:
    digit = temp %10
    sum_digit += digit
    temp=temp//10

print("sum of digit is:", sum_digit)
 