# Appending data to the end of a file
with open("my_file.md", "a") as file:
    file.write("\nThis line is appended at the end.")
    file.write("\nWe preserved the old text!")
    file.write("\nThis file appended by 181.py file")
print("Data appended successfully.")

