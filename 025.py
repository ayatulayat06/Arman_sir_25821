# Demonstrating Identity Operators
list1= [1,2,3]
list2= [1,2,3]
list3= list1

# is operator
print("list1 == list2 (same value?):", list1==list2)
print("list1 is list2 (same object?):", list1 is list2)
print("list1 is list3 (same object?):", list1 is list3)

# is not operator
print("Memory ID of list1:", id(list1))
print("Memory ID of list2:", id(list2))
print("Memory ID of list3:", id(list3))