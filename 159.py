# Storing and displaying student info using dictionary
name = input("Enter Student Name: ")
roll = int(input("Enter Roll Number: "))
gpa = float(input("Enter GPA: "))
student_info = {
 "Name": name,
 "Roll": roll,
 "GPA": gpa
}
print("\n--- Student Bio-Data ---")
for key, val in student_info.items():
 print(f"{key} : {val}")
 