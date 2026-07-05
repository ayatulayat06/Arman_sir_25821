# Swapping two variables using a temporary variable
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

temp = num1
num1 = num2
num2 = temp

print("After swapping: num1 =", num1, "and num2 =", num2)