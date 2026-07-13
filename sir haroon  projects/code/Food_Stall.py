menu = {
    "pizza" : 30.0,
    "burger" : 25.0,
    "fries" : 10.0,
    "popcorn" : 50.0,
    "soda" : 15.0,
    "noodles" : 40.0
}

cart = []
total = 0
print("------------------MENU------------------")

for key,value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------------------")

while True:
    food = input("Select an item or press q to quit: ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

print("------------------YOUR ORDER------------------")    
for food in cart:
    total += menu.get(food)
    print(food, end= " ")
    
print()
print(f"Total is: ${total:.2f}")