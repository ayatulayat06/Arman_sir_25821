# Printing a Pyramid Pattern
N = int(input("Enter height of pyramid: "))
for i in range(1, N + 1):
    print(" " * (N - i) + "* " * i)

