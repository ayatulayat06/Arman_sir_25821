# Sum of numbers divisible by 7 from 1 to N 
N = int(input("Enter N: ")) 
sum = 0 

for i in range(7, N + 1, 7): 
    sum += i
print("sum of number divition up to 7",sum)
