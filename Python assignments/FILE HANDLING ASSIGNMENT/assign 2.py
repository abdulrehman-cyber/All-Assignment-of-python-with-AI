with open("D:\ training_log.txt", "a") as f:
    count=1
    while count <=5:
        print(f"Epoches{count} : training.......")
        count+=1

with open("D:\ training_log.txt","r") as f:
    data=f.read()