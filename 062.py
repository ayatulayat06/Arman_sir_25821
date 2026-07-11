# Printing numbers from N down to 1 in reverse order 
N = int(input("Enter starting number (N): ")) 
print("Countdown from", N, "to 1:") 
for i in range(N, 0, -1): 
    print(i, end=" ") 
