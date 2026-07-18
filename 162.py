# Character frequency calculation using get()
text = input("Enter a word: ")
char_freq = {}
for char in text:
    char_freq[char] = char_freq.get(char, 0) + 1
print("Character Frequencies:")
for char, count in char_freq.items():
    print(f"'{char}' occurred {count} times")


    