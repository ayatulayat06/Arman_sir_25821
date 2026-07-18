# Function to check Palindrome string
def is_palindrome(text):
    clean_text = text.lower()
    return clean_text == clean_text[::-1]


word = "Madam"
if is_palindrome(word):
        print(word, "is a Palindrome")
else:
    print(word, "is NOT a Palindrome")