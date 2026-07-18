# Printing Reverse Pyramid Pattern
N = int(input("Enter height: "))
for i in range(N, 0, -1):
    print(" " * (N - i) + "* " * i)


