# Loops are used to repeat insstructions
# count = 1
# while count <= 10:
#     print("Hello haroon", count)
#     count += 1

# print numbers from 1 to 100
# i = 1
# while i<=100:
#     print(i)
#     i += 1

# WAP to print numbers from 100 to 1
# i = 100
# while i>=1:
#     print(i)
#     i -= 1

# WAP to Print the multiplication table of a number n. take n = 3
# i = 1
# n = 3
# while i <= 10:
#     print("3 x",i, "=", n*i)
#     i += 1

# WAP to print the elements of the following list using loop. 
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# count = 0
# while count < len(nums):
#     print(nums[count])
#     count += 1


# WAP to Search for a number x in this tuple using loop:
# nums = [18, 19, 20, 21, 22, 23, 24, 25]
# myage = 24
# i = 0
# while i < len(nums):
#     if(nums[i]==myage):
#        print("Found at", i)
#     else:
#         print("Finding") 
#     i += 1

# Break : used to terminate the loop when encountered.
# count = 1
# while count <= 10:
#     if(count == 5):
#         break
#     print(count)
#     count += 1

# Continue : terminates execution in the current iteration & continues execution of the loop with the next iteration. In short it is used when you want to skip certain values.
# count = 1
# while count <= 10:
#     if(count == 3):
#         count += 1
#         continue
#     print(count)
#     count += 1

# Print the elements of the following list using a loop: nums = [18, 19, 20, 21, 22, 23, 24, 25]
# nums = [18, 19, 20, 21, 22, 23, 24, 25]
# for i in nums:
#     print(i)

# Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
# nums = (1, 49, 9, 16, 25, 36, 49, 64, 81,100,49)
# x = 49

# idx = 0
# for i in nums:
#     if(i == x):
#         print("Found at index number: ", idx)
#     idx += 1

# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number. range( start?, stop, step?) ? denotes optional parameters

# WAP to print numbers from 1 to 100 using range() and for loop
# seq = range(101)
# for i in seq:
#     print(i)

# WAP to print numbers from 100 to 1 using range() and for loop
# seq = range(100,0,-1)
# for i in seq:
#     print(i)

# WAP to Print the multiplication table of a number n. take n = 4
# seq = range(1,41)
# for i in seq:
#     while i % 4 == 0:
#         print(i)
#         break
# following way is also good
# n = int(input("Enter number to generate table: "))
# for i in range(1,11):
#     print(n*i)

# pass is a null statement that does nothing. It is used as a placeholder for future code.
# seq = range(1,11)
# pass
# print(range)

# WAP to find the sum of first n numbers. (using while)
# n = int(input("Enter number to find sum: "))
# sum = 0
# i = 1
# while i<=n:
#     sum += i
#     i+= 1
# print("Sum of first", n, "numbers is: ", sum)

# WAP to find the factorial of first n numbers. (using for)
# n = int(input("Enter number to find factorial: "))
# factori = 1
# i = 1
# while i<=n:
#     factori *= i
#     i+= 1
# print("Factorial of ", n, "is: ", factori)
