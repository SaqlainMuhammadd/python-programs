#While Loop

# Print numbers from 1 to 100.
i = 1
while i <= 100:
    print(i)
    i += 1

# Print numbers from 100 to 1.

j = 100
while j >= 1:
    print(j)
    j-=1

#Print the multiplication table of a number n.

n = int(input("Enter the Value: "))
k = 1
while k <= 10:
    print(n*k)
    k += 1
    
# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
idx = 0
while idx < len(nums):
    print(nums[idx])
    idx += 1