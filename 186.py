# Counting vowels in a file
with open("my_file.txt", "r") as file:
    text = file.read().lower()
vowels = "aeiou"
vowel_count = sum(1 for char in text if char in vowels)
print("Total vowels in file:", vowel_count)# Copying one file to another
with open("my_file.txt", "r") as src:
 data = src.read()
with open("copy_file.txt", "w") as dest:
 dest.write(data)
print("File copied successfully to 'copy_file.txt'.")