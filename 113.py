# Counting spaces in a string
text = input("Enter a sentence: ")
space_count = 0
for char in text:
    if char == ' ':
        space_count += 1
print("Total white spaces:", space_count)

