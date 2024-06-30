#Write a program to check if a list contains palindrome of elements. 

list1 = list(input('Enter the Palindrome Numbers: '))

list1_copy = list1.copy()
list1_copy.reverse()

if(list1_copy == list1):
    print('This is Palindrome')
else:
    print('This is not Palindrome')