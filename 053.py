# Checking voting eligibility 
age = int(input("Enter your age: ")) 
if age >= 18: 
    print("You are eligible to vote.") 
else: 
    years_left = 18 - age 
print("You are NOT eligible to vote.") 
