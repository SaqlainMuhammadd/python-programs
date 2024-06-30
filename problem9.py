#Student grades

marks = int(input("Enter Student Marks: "))

if(marks >= 90 and marks < 100):
    print("A+ Grade")
elif(marks >= 80 and marks <90):
    print('A Grade')
elif(marks >= 70 and marks < 80):
    print('B+ Grade')
elif(marks >= 60 and marks < 70):
    print('B Grade')
elif(marks >= 50 and marks < 60):
    print('C+ Grade')
elif(marks >= 40 and marks < 50):
    print('C Grade')
elif(marks >= 30 and marks < 40):
    print('D Grade')
else:
    print('Student is fail')