balance = 5000
deposits = 0
withdrawals = 0
while True:
    print("\n1. Deposit 2. Withdraw 3. Balance 4. Summary 5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        amount = float(input("Deposit amount: "))
        if amount > 0:
            balance = balance + amount
            deposits = deposits + 1
            print("Deposit successful")
        else:
            print("Amount must be positive")
    elif choice == "2":
        amount = float(input("Withdrawal amount (maximum Rs. 2000): "))
        if amount <= 0:
            print("Amount must be positive")
        elif amount > 2000:
            print("Withdrawal limit exceeded")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance = balance - amount
            withdrawals = withdrawals + 1
            print("Withdrawal successful")
    elif choice == "3":
        print("Balance: Rs.", round(balance, 2))
    elif choice == "4":
        print("Deposits:", deposits)
        print("Withdrawals:", withdrawals)
        print("Balance: Rs.", round(balance, 2))
    elif choice == "5":
        print("Thank you for using the ATM simulation")
        break
    else:
        print("Invalid option")