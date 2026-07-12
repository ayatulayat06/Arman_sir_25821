# chak the automorphic number
num = int(input("Enter a number: "))

square = str(num * num)

if square.endswith(str(num)):
    print(num, "is an Automorphic Number")
else:
    print(num, "is NOT an Automorphic Number")
    