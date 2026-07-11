# Checking validity of a triangle given three sides 
a = float(input("Enter side 1: ")) 
b = float(input("Enter side 2: ")) 
c = float(input("Enter side 3: "))

if (a + b > c) and (b + c > a) and (a + c > b):
    print("Valid Triangle! A triangle CAN be formed.")
else:
    print("Invalid Triangle! A triangle CANNOT be formed.")