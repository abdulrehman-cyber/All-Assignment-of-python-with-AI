list=[1,2,3,4,5]
for el in list:
    print(el)

print(""" With else""")
for el in list:
    print(el)
else:
    print("End")

    #excercise 
num=(1,2,4,49,5,22,53,49,46,49)
x=49
idx=0
for i in num:
    if(i==x):
        print("find the x number",idx)
    idx+=1


seq= range(101)
for i in seq:
    print(i)

seq= range(100,0,-1)
for i in seq:
    print(i)
