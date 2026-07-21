count=1
with open("marks.txt", "w") as f:
    while count<=5:
        marks=input("Enter the marks : ")
        f.write(marks+"\n")
        count+=1

with open("marks.txt") as f:
    data=f.read()
    print(data)
    