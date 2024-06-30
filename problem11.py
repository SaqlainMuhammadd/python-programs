#Find the greatest number from the numbers user entered

a = int(input("Enter the 1st Number: "))
b = int(input("Enter the 2nd Number: "))
c = int(input("Enter the 3rd Number: "))

if (a>b and a>c):
    print('This is the Greatest number: ', a)
elif(b>c and b>a):
    print('This is the Greatest number: ',b)
elif(c>b and c>a):
    print('This is the Greatest number: ',c)
else:
    print('Enter the Correct Numbers')