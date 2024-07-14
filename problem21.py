# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for el in nums:
    print(el)


# Search for a number x in this tuple using loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

print("Second Question")

Val = (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

x = 16
idx = 0

for el in Val:
    if(el == x):
        print("Element Found at idx", idx)
    idx += 1
else:
    print("Loop Ended")