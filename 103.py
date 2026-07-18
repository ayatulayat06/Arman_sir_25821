# Printing Number Triangle Pattern
N = int(input("Enter height: "))
for i in range(1, N + 1):
    for j in range(1, i + 1):
         print(j, end=" ")
    print()

