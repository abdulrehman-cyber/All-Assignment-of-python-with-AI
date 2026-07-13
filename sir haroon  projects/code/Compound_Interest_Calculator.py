# this is a way of showing the user that on a fixed interest rate, after some time, on a principle amount, how much interest he will pay

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount cannot be less than or equal to zero")
while rate <= 0:
    rate = float(input("Enter rate of interest: "))
    if rate <= 0:
        print("Rate cannot be less than or equal to zero")
while time <= 0:
    time = int(input("Enter the time: "))
    if time <= 0:
        print("Time amount cannot be less than or equal to zero")

total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")
    