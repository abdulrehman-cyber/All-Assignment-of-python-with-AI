import random

myran = random.randint(1,20)

while True:
    userInput = input("Enter your guess betweem 1 and 20 (press q to quit the game): ")
    if(userInput == "q"):
        print("User quit the game!")
        break
    userInput = int(userInput)
    if(userInput == myran):
        print("You won!")
        break
    elif(userInput < myran):
        print("Number too small, try bigger")
    else:
        print("Number too big, try smaller")

