# Storing multiple student records in a file
students = [
    {"roll": 1, "name": "Akil", "gpa": 3.80},
    {"rool": 2, "name": "Ayat", "gpa": 3.96},
    {"roll": 3, "name": "Karim", "gpa": 3.90},
    {"roll": 4, "name": "Sadiya", "gpa": 4.00},
    {"rool": 5, "name": "Jedan", "gpa": 3.86}
]
with open("students.txt", "w") as file:
    file.write("Roll | Name | GPA\n")
    file.write("---------------------\n")
    for s in students:
        file.write(f"{s['roll']} | {s['name']:<6} | {s['gpa']}\n")
print("Student records saved to 'students.txt'.")