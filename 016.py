# Swapping without temporary variable (Pythonic way)
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")

print("Before swapping: num1 =", num1, "and num2 =", num2)

# Swapping without temp
num1, num2 = num2, num1
print("After swapping: num1 =", num1, "and num2 =", num2)