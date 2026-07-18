# Writing new data into a file (Overwriting existing content)
with open("my_file.md", "w") as file:
    file.write("This is completely new text.\n")
    file.write("Previous contents have been overwritten.\n")
    file.write("this file update by Ayat.(program no 180.py)")
print("New data written successfully.")

