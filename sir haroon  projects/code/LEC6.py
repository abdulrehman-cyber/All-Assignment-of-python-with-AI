# Funcions in python are block of statements that perform a specific task. print(), len(), type() and range() are pre-defined functions in python.
# def sum(a,b):
#     s = a + b
#     return s
# print(sum(2,3))

# create a function to print the average of three numbers
# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# c = int(input("Enter third number: "))
# def calcavg(a,b,c):
#     avg = (a + b + c) / 3
#     return avg
# print("The avg of three numbers: ",calcavg(a,b,c))

# WAF to print the length of the list
# def prli():
#     li = ["a","b","c","d"]
#     print(len(li))
#     return len(li)
# prli()

# WAF to print the elements of a list in a single line. ( list is the parameter)
# def prli():
#     li = [1,2,3,4,5]
#     for i in li:
#         print (i, end = " ")
# prli()

# WAF to find the factorial of n. (n is the parameter)
# def factori(a):
#     fact = 1
#     for i in range(1,a+1):
#         fact *= i
#     print(fact)

# a = int(input("Enter the number to find factorial: "))
# factori(a)

# WAF to convert USD to PKR
# def converter(usd_val):
#     pkr_val = usd_val * 278
#     print(usd_val, "USD = ", pkr_val, "PKR")
#     return pkr_val

# usd_val = int(input("Enter dollara amount to convert to pkr: "))
# converter(usd_val)

# Recursion means when a function calls itself repeatedly. Below is an example of recursive function
# def show(n):
#     if(n==0):
#         return
#     print(n)
#     show(n-1)
# show(7)

# Lets see factorial using recursion function
# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(5))

# WAF to print the sum of first n natural numbers
# def cal_sum(n):
#     if(n==0):
#         return 0
#     return cal_sum(n-1) + n 
# sum = cal_sum(100)
# print(sum)

# Write a recursive function to print all elements in a list. Hint: use list & index as parameters
# def prli(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     prli(list,idx+1)
# li = [1,2,3,4,5,6,7]
# prli(li)
