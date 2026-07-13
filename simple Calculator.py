num1=float(input("Enter First Number : "))
op=input("Enter The Operator (+, -, *, /):  ")
num2=float(input("Enter Second Number : "))
if op == "+":
    print("Sum :", num1+num2)
elif op == "-":
    print("subtract:", num1 - num2)
elif op == "*":
    print("multiply : ", num1*num2)
elif op == "/":
    print("divide :", num1/num2)
else:
    print("invailid operator")