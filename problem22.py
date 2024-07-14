#WAP to find the sum of first n numbers. using for loop

num = int(input("Enter Value :"))

x = 0
for i in range(0, num+1):
    x += i
print("Total sum is :", x)

#using while loop

n = int(input("Enter Value :"))
sum = 0
i = 1

while i <= n:
    sum += i
    i += 1
print("Total sum is equal to : ", sum)