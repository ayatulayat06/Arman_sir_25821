sum = 0
for i in range(3,100,3):
    sum += i**2

print("Sum of the sirise: ",sum)
print("sum:",sum(i**2 for i in range (3,100,3)))

