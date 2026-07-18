# Copying one file to another
with open("my_file.txt", "r") as src:
    data = src.read()
with open("copy_file.txt", "w") as dest:
    dest.write(data)
    
print("File copied successfully to 'copy_file.txt'.")

