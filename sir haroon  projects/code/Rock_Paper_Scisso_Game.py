import random

options = ("rock", "paper", "scissor")
running = True

while running:
    player = None 
    computer = random.choice(options)
    while player not in options:
        player = input("Enter a choice between rock,paper and scissors: ")
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        if player == computer:
            print("Its a TIE!")
        elif player == "rock" and computer == "scissor":
            print("You Win!")
        elif player == "paper" and computer == "rock":
            print("You Win!")
        elif player == "scissor" and computer == "paper":
            print("You Win!")
        else:
            print("You Lose!")
        if not input("Play Again? (y/n): ").lower() == "y":
            running = False
        print("Thanks for playing!")
