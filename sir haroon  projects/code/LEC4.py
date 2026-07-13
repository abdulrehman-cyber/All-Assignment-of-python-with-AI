# Dictionories in python are used to store data values in key:value pairs. They are unordered, mutable and do not allow suplicate keys. below is an example of a dictionary. note that parents-info is called nested dictionary. To only print nested dictionary, use [key], [parents-info] in this case.

info = {
    "id" : 1,
    "name" : "arsal",
    "is-adult" : False,
        "Parents-info" : {
            "Father Name" : "Jafar khan", 
            "Mother Name":"Maryam"
            }
}
# print(info["Parents-info"])

# Following are some methods of dictionary

# returns all keys  
# print(info.keys())

# returns all values
# print(info.values())

# returns all key value pairs as tuple
# print(info.items())

# returns the key according to value
# print(info.get("name"))

# inserts the specified items in dictionary
# info.update(
#     {
#         "city" : "Lahore"
#     }
# )
# print(info)

# Set is the colletion of unordered items. Each element in the set must be unique and immutable.list and dictionary are not allowed in sets while tuples are allowed

# num = {1,2,3,4,5,5,5,5}
# print(type(num))
# print(num)

# collection = set()
# print(collection)
 # to print an empty set collection =  set() print(collection)

# set methods
# nums = {1,2,3,4,5.32,6,7,8,9}
# nums.add("haroon")
# nums.remove(2)
# nums.pop() # removes any random element from the set
# nums.clear() # empties the whole set
# set1 = {1,2,3,4,5,4,3,2}
# set2 = {9,8,7,6,0,2,3,4}
# print(set1.union(set2))
# print(set1.intersection(set2))

"""-------------------------------------------------------"""

# WAP to Store following word meanings in a python dictionary :
# table : “a piece of furniture”,“list of facts & figures”
# cat : “a small animal”

# dict = {
#     "table" : "a piece of furniture,list of facts & figures",
#     "cat" : "a small animal"   
# }
# print(dict)


#  You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students. "python","java","C++","python","javascript","java","python","java","C++","C"
# classroom = {"python","java","C++","python","javascript","java","python","java","C++","C"}
# print(len(classroom))

# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

# eng = int(input("Enter English marks:"))
# math = int(input("Enter Maths marks:"))
# geo = int(input("Enter Geography marks:"))

# mydict = {}
# mydict.update(
#     {
#     "English" : eng,
#     "Maths" : math,
#     "Geography" : geo,
#     }
# )
# print(mydict)

# below code is also good
# mydict = {}
# mydict["English"] = int(input("Enter English marks: "))
# mydict["Maths"] = int(input("Enter Maths marks: "))
# mydict["Geography"] = int(input("Enter Geography marks: "))

# Figure out a way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
# myset = {
#         "integer" : 9,
#         "float" : 9.0    
#         }
# print(myset)