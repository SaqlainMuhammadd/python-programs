# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

#First possible solution

Values = {
    "9", 9.0
}
print(Values)

#second solution using touples

Val = {
    ('Float' , 9.0),
    ('int', 9)   
}
print(Val)