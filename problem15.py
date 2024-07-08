#Store following word meanings in a python dictionary : 
# table : “a piece of furniture”, “list of facts & figures”
#  cat : “a small animal”

dict = {
    "table" : {
        "a piece of furniture", "list of facts & figures"
        },
    "cat" : "a small animal"
}
print(dict)

# You are given a list of subjects for students. Assume one classroom is required for 1
# subject. How many classrooms are needed by all students.
# ”python”,“java”,“C++”,“python”,“javascript”,"java",“python”,“java”,“C++”,“C”

Classroom = {
    "Python", "Java", "C++", "Python", "JavaScript", "Java", "Python", "Java", "C++", "C"
}

print("The Number of Classroom needed for Students are: ", len(Classroom))
print(type(Classroom))