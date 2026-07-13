class Car:
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price
car1 = Car("Honda", 3500000)
car2 = Car("Toyota", 2500000)

print(car1.brand, car1.price)

print(car2.brand, car2.price)
