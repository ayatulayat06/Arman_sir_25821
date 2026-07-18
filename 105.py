N = int(input("Enter height: "))
for i in range(1, N + 1):
    for j in range(i):
        char = chr(65 + j)
        print(char, end=" ")
    print()