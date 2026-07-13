class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_detail(self):
        return (f"{self.name}: {self.salary}")

emp1 = Employee("Abdul", 40000)
emp2 = Employee("Adil", 45000)

print(emp1.show_detail())
print(emp2.show_detail()) 

        