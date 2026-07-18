# Reversing a string using loop
text = input("Enter a string: ")
rev_text = ""
for char in text:
    rev_text = char + rev_text
print("Reversed string is:", rev_text)


