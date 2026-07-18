# Storing and searching multiple student results
results = {
    101: {"name": "Ayat", "gpa": 3.85},
    102: {"name": "Akil", "gpa": 3.60},
    103: {"name": "Sadiya", "gpa": 4.00}
}


search_roll = int(input("Enter Roll Number to check result (101-103): "))
if search_roll in results:
    info = results[search_roll]
    print(f"Name: {info['name']} | GPA: {info['gpa']}")
else:
    print("Result not found for this Roll Number!")

