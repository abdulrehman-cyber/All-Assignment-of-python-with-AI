# File I/O in python: Python can be used to perform operations on a file. (read & write data)
# Types of all files: 1) Text Files: .txt .docx .ppt 2) Binary Files: .mp4 .mov .png

# To open a file in python, use the following code. here, first arguement shows file name and second shows mode. r for read and w for write
# f = open('LEC1.py', 'r')
# data = f.read()
# print(data)
# f.close()

# with automatically closes the file
# with open('LEC2.py', 'r') as f:
#     data = f.read()
#     print(data)

# below is the way of deleting files in python
# import os
# os.remove(LEC1.py)

# Create a new file “practice.txt” using python. Add the following data in it:
# Hi everyone
# we are learning File I/O
# using Java.
# I like programming in java

# f = open("demo.txt", "w")
# f.write("Hi everyone \n we are learning File I/O \n")
# f.write("using java \n I like programming in java \n" )

# WAF that replace all occurrences of “java” with “python” in above file
# with open("demo.txt", "r") as f:
#     data = f.read()

# new_data = data.replace("java", "python")
# print(new_data)

# with open("demo.txt", "w") as f:
#     data = f.write(new_data)

# Search if the word “learning” exists in the file or not
# def check_for_word():
#     word = "learning"
#     with open("demo.txt", "r") as f:
#         data = f.read()
#         if(data.find(word) != -1):
#             print("Found")
#         else:
#             print("not found")
# check_for_word()

# From a file containing numbers separated by comma, print the count of even numbers
# count = 0
# with open("demo.txt", "r") as f:
#     data = f.read()
#     nums =  data.split(",")
#     for val in nums:
#         if(int(val) % 2 == 0):
#             count += 1
# print(count)
