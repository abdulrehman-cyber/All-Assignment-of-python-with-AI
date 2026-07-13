weight = float(input("Enter your weight in number: "))
unit = input("Enter your weight unit K for kilograms , L for pounds: ")
if unit == "K":
    weight *= 2.205
    unit = "lbs"
    print(f"Your weight is {round(weight,1)}{unit}")

elif unit == "L":
    weight /= 2.205
    unit = "kg"
    print(f"Your weight is {round(weight,1)}{unit}")

else:
    print(f"{unit} was not valid!")
