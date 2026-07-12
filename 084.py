# palindrome number

num = int(input("Enter a number: "))

original_num = num
reverse_num = 0

while num > 0:
    digit = num % 10          # শেষ digit বের করার জন্য 
    reverse_num = reverse_num * 10 + digit
    num //= 10                # শেষ digit বাদ দেয়ার জন্য

if original_num == reverse_num:
    print(original_num, "is a Palindrome Number")
else:
    print(original_num, "is NOT a Palindrome Number")
 