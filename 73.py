print("Looping from 1 to 10, but stopping when 5 is reached:")
for i in range(1, 11):
    if i == 5:
        print("\nCondition (i == 5) met! Breaking the loop.")
    break
print(i, end=" ")
print("Program finished.")