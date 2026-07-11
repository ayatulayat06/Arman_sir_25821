# Sum of Even numbers from 1 to N 
N = int(input("Enter N: ")) 
sum = 0 
for i in range(2, N + 1, 2): 
    sum += i 
print("Sum of even numbers from 1 to", N, "is:", sum)
