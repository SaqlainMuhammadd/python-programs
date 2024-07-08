# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

x = 81

idx = 0
while idx < len(nums):
    if(nums[idx] == x):
        print("Found at idx ", x)
        break
    else:
        print("Finding...")
    idx += 1 
print("End of Loop")