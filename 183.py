# Counting total words in a file
with open("my_file.md", "w") as f:
    f.write("Python is a powerful and easy programming language.")
with open("my_file.txt", "r") as file:
    content = file.read()
    words = content.split()
    print("Total words in file:", len(words))

