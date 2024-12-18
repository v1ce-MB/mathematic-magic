number=int(input("Enter the number:"))
length = len(str(number))

temp=number

sum=0

while temp>0:
    digit=temp % 10
    sum+=digit**length
    temp=temp//10

if number == sum:
    print("this is an armstrong number")
else:
    print("this is not an armstrong number")
    