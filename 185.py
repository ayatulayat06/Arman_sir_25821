# Counting characters in a file
with open("my_file.txt", "r") as file:
    content = file.read()
    print("Total characters in file:", len(content))


