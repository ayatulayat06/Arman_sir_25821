# Counting lines in a file
with open("sample_lines.txt", "w") as f:
    f.write("Line 1: Hello\nLine 2: Python\nLine 3: World")
with open("sample_lines.txt", "r") as file:
    lines = file.readlines()
    print("Total lines in file:", len(lines))

    