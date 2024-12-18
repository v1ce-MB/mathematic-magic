number= int(input("enter the number to find factors: "))
for i in range (1,number+1):
    if (number % i == 0):
      print(i)