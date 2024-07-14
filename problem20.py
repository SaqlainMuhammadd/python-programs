# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

# idx = 0
# while idx < len(nums):
#     print(nums[idx])
#     idx += 1

# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

num = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

x = 36
i = 1

while i < len(num):
    if(num[i] == x):
        print("Found x at index:", i)
        break
    else:
        print("Finding")
print("Loop Ended")