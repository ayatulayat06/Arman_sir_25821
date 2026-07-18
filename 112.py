# Counting digits in a string
text = input("Enter a string with numbers: ")
digit_count = 0
for char in text:
    if char.isdigit():
        digit_count += 1
print("Total digits in the string:", digit_count)
