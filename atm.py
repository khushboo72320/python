balance = 1000

while True:
    print("\n----- ATM PROFILE -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance =", balance)

    elif choice == 2:
        amount = int(input("Enter deposit amount: "))
        balance += amount
        print("Amount Deposited Successfully")

    elif choice == 3:
        amount = int(input("Enter withdrawal amount: "))
        
        if amount <= balance:
            balance -= amount
            print("Please collect your payment")
        else:
            print("Insufficient Balance")

    elif choice == 4:
        print("Thanks")
        break

    else:
        print("Invalid Choice")
