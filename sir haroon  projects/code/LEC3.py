# mylist = [1,"haroon",0.4,999999999999,"4ali",6,7,8,9] # mylist is a data-type in python. it can be changed
# print(type(mylist))

# mylist methods
# mylist.append(8) # adds one element at the end 
# mylist.sort() # sorts in ascending order
# mylist.sort(reverse=True) # sorts in descending order
# mylist.reverse() # reverses mylist
# mylist.insert(5,99) # insert element at index
# mylist.remove(3) # will remove 3rd occurrence from our mylist
# mylist.pop(4) # will remove the index number 4
# print(mylist)


# tuple is a built in data-type that lets us create immutable sequences of values
# mytuple = (0,"haroon",2,3.0,4,5,5,5,5)
# print(mytuple.index("haroon")) # it always returns the index value on which the elment you are searching is present
# print(mytuple.count(5)) # it shows how many times an element (you used) is present in the tuple

"""---------------------------------------------------------------------------------------------"""
# WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
# userinput = [input("Enter your top 1 favorite movies name:"), input("Enter your top 2 favorite movies name:"), input("Enter your top 3 favorite movies name:")]
# print(userinput)

# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

# list_1 = [1,2,1,1,1]
# list_1_copy = list_1.copy()
# list_1.reverse()

# if(list_1_copy == list_1):
#     print("ITS A PALINDROME")
# else: 
#     print("NOT A PALINDROME")

# WAP to count the number of students with the “A” grade in the following tuple. 
# Also store the values in list and sort from A to D.

# list = ["C", "D", "A", "A", "B", "B", "A"]
# print("Number of students who got an A is: ", list.count("A"))
# list.sort()
# print("List in ascending order:", list)