# Question no 1:
allowed_age=[18,19,20,21,22]
user=int(input("enter the age : "))
if user in allowed_age:
    print("you entered age is exist")
else:
    print("not exist")

# Question no 2:

import random
score_list=[]
for i in range(5):
    accuracy=random.randint(60,100)
    score_list.append(accuracy)
print("accuracy = ",score_list)
if 90 in score_list:
    print("90 is found")
else:
    print("90 not found")

