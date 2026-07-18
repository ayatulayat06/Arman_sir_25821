N = int(input("Enter a sirise "))
total = 0


for x in range(2,N+1,2):
    total += x**2

print("sum of the N serise:",total)

print("sum:",sum(x**2 for x in range(2,N+1,2)))

