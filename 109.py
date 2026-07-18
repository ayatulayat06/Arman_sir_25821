# Checking string Palindrome
text = input("Enter a word: ").lower()
rev_text = text[::-1]
if text == rev_text:
    print("It is a Palindrome")
else:
    print("It is NOT a Palindrome")


