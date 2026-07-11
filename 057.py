# Checking Uppercase or Lowercase 
char = input("Enter an alphabet character: ")
if 'A' <= char <= 'Z':
    print(char, "is an UPPERCASE character")
elif 'a' <= char <= 'z':
    print(char, "is a lowercase character")
else:
    print(char, "is not an alphabet character")