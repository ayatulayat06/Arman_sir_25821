# Reading entire content from a file
try:
    with open("my_file.md", "r") as file:
        content = file.read()
    print("--- File Content ---")
    print(content)
except FileNotFoundError:
    print("Error: The specified file does not exist!")

