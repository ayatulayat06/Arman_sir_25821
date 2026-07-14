N = int(input("Enter N of number: "))

sum=0
for i in range(1,N+1,1):
    sum+=i**2
    print("i:",i," i_squire:", i**2, " Sum:", sum)

print("Sum of the serise is: ",sum)