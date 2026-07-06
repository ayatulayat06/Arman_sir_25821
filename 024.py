# Demonstrating Logical Operators

age= int(input("Enter your age: "))
has_id= input("Do you have an ID? (yes/no): ")== "yes"

# AND operetor Condition check must be true for both conditions to be true
cen_center= (age >= 18) and has_id
print("can enter restricted area (age >=18 AND has ID): ", cen_center)

# Or operetor; condition cheak must be true
discount= (age>= 18) or (age<60)
print("Eligible for discount (age >=18 OR age <60): ", discount)

# NOT operator; condition check must be false
not_eligible= not (age>= 18)
print("Not eligible for discount (NOT age >=18): ", not_eligible)