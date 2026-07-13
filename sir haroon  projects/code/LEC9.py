# del keyword is used to delete object properties or object itself for example del s1.name
# class Student():
#     def __init__(self, name):
#         self.name = name 
        
# prStd = Student("Arsal")
# print(prStd.name)
# del prStd.name
# print(prStd.name)

# to make any attribute private use __

# Inheritance
# class Car:
#     @staticmethod
#     def start():
#         print("car started...")

#     @staticmethod
#     def stop():
#         print("Car stopped.")

# class ToyotaCar(Car):
#     def __init__(self, name):
#         self.name = name

# car1 = ToyotaCar("fortuner")
# car2 = ToyotaCar("prius")

# print(car1.start())

# class Student:
#     def __init__(self,phy,chem,math):
#         self.phy = phy
#         self.chem = chem
#         self.math = math

#     @property
#     def percentage(self):
#         return str((self.phy + self.chem + self.math) / 3) + "%"
    
# std1 = Student(98,97,95)
# print(std1.percentage)

# std1.phy = 56
# print(std1.percentage)

# __add__ is called a dunder function

# Define a circle class to create a circle with radius r using constructor. use area = pi r square  Define an area() method of the class  which calculates the area of the circle. 
# Define a parameter() method of the class which allows you to calculate the perimeter of the circle. use formula 2 pi r

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return 3.14 * self.radius ** 2
    
#     def perim(self):
#         return 2 * 3.14 * self.radius

# c1 = Circle(5)
# print(c1.area())
# print(c1.perim())

# Define a Employee() class with attributes role, department and salary
# Create an Engineer class that inherits properties from Employee & has additional attributes : name & age
# class Employee():
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role = ", self.role)
#         print("department = ", self.dept)
#         print("salary = ", self.salary)
        

# class Engineer(Employee):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         super().__init__("Engineer", "IT", "65,000")

# engg1 = Engineer("Elon Musk", 40)
# engg1.showDetails()

# Create a class Order which stores item and its price. Use Dunder function __gt__() to convey that order1 > order2 if price of order1 > price of order2
# class Order:
#     def __init__(self, item, price):
#         self.item = item 
#         self.price = price
#     def __gt__(self, ord2):
#         return self.price > ord2.price
    
# obj1 = Order("chips", 65)
# obj2 = Order("biscuits", 20)

# print(obj1 > obj2)
