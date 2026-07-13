def show_balance(balance):
    print(f"Your current balance is ${balance:.2f}")
    # print("*************************************")

def deposit():
    print("-----------------------")
    amount = float(input("Enter an amount to deposit: "))
    print("-----------------------")

    if amount < 0:
        print("Please enter a valid amount")
        return 0
    else:
        return amount

def withdraw(balacne):
    print("-----------------------")
    amount = float(input("Enter an amount to be withdrawn: "))
    print("-----------------------")

    if amount > balacne:
        print("Insufficient Funds!")
        return 0
    elif amount < 0:
        print("Amount cannot be less than zero")
        return 0
    else:
        return amount
    
def main():
    balance = 0
    is_running = True

    while is_running:
        print()
        print("***********************")
        print("       PYTHON BANK     ")
        print("***********************")

        print("-----------------------")
        print("1. Show Current Balance")
        print("2. Deposit Cash")
        print("3. Withdraw Cash")
        print("4. Exit")
        print("-----------------------")

        choice = input("Enter your Choice (1,2,3,4): ")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance += deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
    else:
        print("***********************")
        print("Please enter a choice from given numbers 1,2,3,4 ")
        print("***********************")

    print("***********************")
    print("Thank You! Have a nice day...")
    print("***********************")

if __name__ == "__main__":
    main()