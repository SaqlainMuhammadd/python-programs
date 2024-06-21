# Find The Square root

#Solution-1 Using Exponentiation

num = int(input('Enter the Value: '))
sr = num**(1/2)

print('The Square root of given number is: ', sr)

#Solution-2 using math Module

import math
num = int(input('Enter the Value: '))
sr = math.sqrt(num)
print('The Square root of given number is: ', sr)
