# Finding sum of numbers from 1 to N 
N = int(input("Enter N: ")) 
total = 0 
for i in range(1, N + 1): 
    total += i 
print("The sum from 1 to", N, "is:", total) 
