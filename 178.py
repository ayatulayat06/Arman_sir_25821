# Creating a new text file using 'w' mode
with open ("my_file.txt", "w") as file:
    file.write("Welcome to Python File Handling!\n")
    file.write("This file was created programmatically.\n")
    file.write("This file was creates 178's program file")

with open("my_file.md", "w") as file:
    file.write("Welcome to Python File Handling!\n")
    file.write("This file was created programmatically.\n")
    file.write("This file was creates 178's program file")
print("File 'my_file.txt' created successfully!")

