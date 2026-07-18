# Searching a word inside a file line by line
with open("story.txt", "w") as f:
    f.write("file created by 190.py\nPython is very popular.\nMany developers love Python.\nJava is also widely used.\nPython makes automation easy.")
search_word = "Python"
found_lines = []
with open("story.txt", "r") as file:
    for line_num, line in enumerate(file, 1):
        if search_word.lower() in line.lower():
            found_lines.append((line_num, line.strip()))
print(f"Search results for '{search_word}':")
if found_lines:
    for num, text in found_lines:
        print(f"Line {num}: {text}")
else:
        print("Word not found in the file.")

        