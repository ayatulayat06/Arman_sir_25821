# Merging two files into a third file
with open("f1.txt", "w") as f: f.write("Part 1: Hello world from file 1.\n")
with open("f2.txt", "w") as f: f.write("Part 2: Welcome Ayatfrom file 2.\n")



# Reading both
with open("f1.txt", "r") as f1, open("f2.txt", "r") as f2:
 data1 = f1.read()
 data2 = f2.read()


# Merging
with open("merged.txt", "w") as m:
 m.write(data1 + data2)
print("Files merged successfully into 'merged.txt'.")