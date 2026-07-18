# Deleting items from a Dictionary
student = {"name": "Abdur Rahman", "age": 22, "district": "Dhaka", "grade": "A"}
print("Before deletion:", student)


# Using del keyword
del student["grade"]


# Using pop() method
removed_val = student.pop("age")
print("After deleting 'grade' and 'age':", student)
print("Removed age value:", removed_val)

