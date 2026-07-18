# Saving and Reading Student Results from File
# Step 1: Saving results
with open("results.txt", "w") as file:
    file.write("This file crerated 189.py program file")
    file.write("101,Abdur Rahman,A+\n")
    file.write("102,Sadiya Islam,A\n")
    file.write("103,Tanvir Ahmed,A+\n")
# Step 2: Reading and formatting results
print("--- Result Sheet ---")
print("Roll | Name | Grade")
print("----------------------------")
with open("results.txt", "r") as file:
    for line in file:
        roll, name, grade = line.strip().split(",")
        print(f"{roll:<4} | {name:<13} | {grade}")

        