print("""                               (STRING FUNCTION)                             """)



text="i am AI Engineer"
print("text= ",text)

print("Capitalize the first alphabet =", text.capitalize())
print("count of e alphabet = ",text.count("e"))
print("Find the word =",text.find("Engineer"))
print("Replace the  word =", text.replace("Engineer","Developer"))
print("Check the last alphabet by using endwith = ",text.endswith("er"))



print("""                     \n\t\t\t\t\t(lIST FUNCTION)                  """)



list=[1,2,4,3,5,6,2,7,8,9]
print("list=",list)
list.append(10)
print("append=",list)
list.sort()
print("acending order =",list)
list.sort(reverse=True)
print("decending order =",list)
list.reverse()
print("reverse list =",list)
list.insert(2,11)
print("Insert a given value in 2 index =",list)
list.remove(2)
print("Remove the value by given =",list)
list.pop(6)
print("pop the value by given index",list)


print("""                   \n\t\t\t\t\t(TUPLE FUNCTION)                    """)

my_tup=(1,3,5,3,4,6,3,4,10)
print("my_tup =",my_tup)
print("length of my_tup =",len(my_tup))
print("index of 5 =",my_tup.index(5))
print("count of 3 =",my_tup.count(3))
print("maximum number of my_tup =",max(my_tup))
print("minimum number of my_tup =",min(my_tup))


print("""               \n\t\t\t\t\t(DICTIONARY FUNCTION)                 """)
student_info={
    "name":"Abdul",
    "age": 26,
    "city":"Lahore",
    "course":"AI",
}
print("student_info =",student_info)
print("keys of student_info = ",student_info.keys())
print("values of student_info = ",student_info.values())
print("items of student_info = ",student_info.items())
print("get the value of age =",student_info.get("age"))
student_info.update({"DOB": "03/06/2000"})
print("update student_info =",student_info)
print("get the value of name =",student_info.setdefault("name"))
print("pop the value of age =",student_info.pop("age"))
print("popitem of student_info =",student_info.popitem())
print("clear the student info =",student_info.clear())
print("copy the student info =",student_info.copy())


print("""         \n\t\t\t\t\t(SET FUNCTION)    """)
set1={1,4,6,2,5,3,2,5,7,8,0}
set2={10,4,3,2,6,7,8,1,9,4,3,5}
print("set1 =",set1)
print("set2 =",set2)
set1.add(11)
print("Add element by using add function =",set1)
set2.pop()
print("pop the element by using pop function =",set2)
set1.remove(0)
print("remove the element by using remove function =",set1)
print("union of set1 and set2 =",set1.union(set2))
print("intersection of set1 and set2 =",set1.intersection(set2))
set1.clear()
set2.clear()
print("clear the set1 =",set1)
print("clear the set2 =",set2)