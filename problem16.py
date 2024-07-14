# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value.

marks = {}

x = int(input("Enter Physics marks: "))
marks.update({
    "Phy" : x
})

x = int(input("Enter Chem marks: "))
marks.update({
    "Chem" : x
})

x = int(input("Enter Math marks: "))
marks.update({
    "Math" : x
})

print(marks)