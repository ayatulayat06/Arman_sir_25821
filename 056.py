# Checking Vowel or Consonant 

char = input("Enter an alphabet character: ")

# Convert to lower case to handle both uppercase and lowercase 
lower_char = char.lower() 

print(lower_char)

if lower_char in ['a', 'e', 'i', 'o', 'u']: 
    print(char, "is a Vowel") 

elif lower_char.isalpha(): 
    print(char, "is a Consonant") 
else: 
    print("Invalid input! Please enter an alphabet.")