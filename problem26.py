# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O 
# using Java.
# I lik in progranmming in Java.


with open("practice.txt", "w") as f:
    f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI lik in progranmming in Java.")

# WAF that replace all occurrences of “java” with “python” in above file.

with open("practice.txt", "r") as f:
    data = f.read()
    new_data = data.replace("Java", "Python")

with open("practice.txt", "w") as f:
    f.write(new_data)

# Search if the word “learning” exists in the file or not.

word = "learning"
with open("practice.txt", "r") as f:
    data = f.read()
    if (data.find(word) != -1):
        print("Found")
    else:
        print("Not Found")

