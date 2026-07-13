unit = input("Is the temprature in Celcius or Fahrenheit (C/F): ")
temp = float(input("Enter the temprature without unit: "))

if unit == "C":
    temp = round((9*temp)/5+32,1)
    print(f"The temprature in Fahreneheit is: {temp} °F", )

elif unit == "F":
    temp = round((temp - 32)* 5/9,1)
    print(f"The temprature in Celcius is: {temp} °C", )

else:
    print(f"{unit} is an invalid unit of measurement")
