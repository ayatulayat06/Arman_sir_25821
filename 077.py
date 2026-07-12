# Finding GCD using Euclidean Algorithm
num1= int(input("Enter your fast number: "))
num2= int(input("Enter your secound number: "))

a, b = num1, num2 
while b != 0: 
    a, b = b, a % b 
print("The GCV of ", num1, "and", num2,"is", a)
