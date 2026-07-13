# OOP in Python
# class Student:
#     def __init__(self, fullname):
#         self.name = fullname
#         print("Adding new student...")

# s1 = Student("Arsal")
# print(s1.name)

# Create student class that takes name & marks of 3 subjects as arguments in constructor.Then create a method to print the average
# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print("hi", self.name, "your avg marks is:", sum/3)

# s1 = Student("arsal jafar", [89,78,88])
# s1.get_avg()

# Create Account class with 2 attributes - balance & account no.Create methods for debit, credit & printing the balance.

# class Account():
#     def __init__(self, bal, acc):
#         self.acc_balance = bal
#         self.acc_no = acc

#     def debit(self,amount):
#         self.acc_balance -= amount
#         print("RS.", amount, "was debitted")
#         print("Total balance left: ", self.get_balance())

#     def credit(self,amount):
#         self.acc_balance += amount
#         print("RS.", amount, "was creditted")
#         print("Total balance left: ", self.get_balance())

#     def get_balance(self):
#         return self.acc_balance

# acc1 = Account(10000, 54321)
# acc1.debit(3000)
# acc1.credit(1000)

