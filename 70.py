num = int(input("Enter a positive integer: "))
count = 0
temp = abs(num)  
if temp == 0:
    count = 1
else:
    while temp > 0:
        temp = temp // 10
        count += 1
print("Total number of digits:", count)