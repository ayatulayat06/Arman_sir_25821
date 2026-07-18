# Counting consonants in a string
text = input("Enter a string: ").lower()
vowels = "aeiou"
consonant_count = 0
for char in text:
    if char.isalpha() and char not in vowels:
        consonant_count += 1
print("Total consonants:", consonant_count)


