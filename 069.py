# Numbers divisible by both 3 and 5
n = int(input("Enter the value of n: "))
for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i, end=" ")
