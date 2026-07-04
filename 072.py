num =int(input("Enter a number"))
temp=abs(num)
rev_num=0
while temp >0:
    digit=temp % 10
    rev_num =(rev_num*10)+digit
    temp=temp // 10

if num <0:
    rev_num=-rev_num

print("reversed number is:",rev_num)
