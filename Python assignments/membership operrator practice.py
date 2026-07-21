# student={
#     "name": "ali",
#     "marks": 85
# }
# print("marks" in student)


#example 1
# list=[5,10,15,20,25]
# user=int(input("enter the number: "))
# if user in list:
#     print("Found")

# else:
#     print("not found")


# import random
# num_list=[]
# for i in  range(10):
#     numbers=random.randint(1,50)
#     num_list.append(numbers)
# print(num_list)
# if 25 in num_list:
#     print("found")
# else:
#     print("not found")


num_list=[]
user_num=int(input("enter the number : "))
while user_num <=5:
    user_num.append(num_list)
check_num=int(input("Enter the number : "))
if check_num in num_list:
    print("found")
else:
    print("not found")