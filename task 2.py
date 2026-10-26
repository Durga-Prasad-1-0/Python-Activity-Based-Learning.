balance = 5000
transactions = []

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            transactions.append(("Deposit", amount))
            print("Deposit successful")
        else:
            print("Invalid amount")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount")
        elif amount > balance:
            print("Insufficient balance")
        else:
            balance -= amount
            transactions.append(("Withdrawal", amount))
            print("Withdrawal successful")

    elif choice == "3":
        print("Current balance: Rs.", balance)

    elif choice == "4":
        break

    else:
        print("Invalid choice")

print("\nTransaction Summary")
for transaction, amount in transactions:
    print(transaction, ": Rs.", amount)

print("Final balance: Rs.", balance)
