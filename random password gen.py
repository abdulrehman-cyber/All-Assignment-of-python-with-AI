import random
import string

pass_len= 8

char_Value= string.ascii_letters + string.digits + string.punctuation

password = " "

for i in range(pass_len):
    password+= random.choice(char_Value)

print("your random pasword is : ", password)