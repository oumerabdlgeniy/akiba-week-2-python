
Pin = "12345"
balance = 1000
count = 3
transaction_count = 0

for i in range(3):
    n = input("Enter your PIN: ")

    if n == Pin:
        print("PIN correct!")
        print("Welcome to Akiba Bank.")

        while True:
            print(
                "\n===== AKIBA BANK =====\n"
                "1. Check Balance\n"
                "2. Deposit Money\n"
                "3. Withdraw Money\n"
                "4. Exit"
            )

            try:
                choice = int(input("Choose an option: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if choice == 1:
                print("Current balance:", balance, "Birr")

            elif choice == 2:
                try:
                    amount = float(input("How much money do you want to deposit? "))
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    continue

                if amount > 0:
                    balance += amount
                    transaction_count += 1
                    print("Deposit successful!")
                    print("Your new balance:", balance, "Birr")
                else:
                    print("Invalid amount!")

            elif choice == 3:
                try:
                    amount = float(input("How much money do you want to withdraw? "))
                except ValueError:
                    print("Invalid amount. Please enter a number.")
                    continue

                if amount > 0:
                    if amount <= balance:
                        balance -= amount
                        transaction_count += 1
                        print("Withdrawal successful!")
                        print("Your new balance:", balance, "Birr")
                    else:
                        print("Insufficient balance!")
                else:
                    print("Invalid amount!")

            elif choice == 4:
                print("Transactions made:", transaction_count)
                print("Thank you for using Akiba Bank!")
                print("Goodbye!")
                break

            else:
                print("Invalid option.")
                print("Please choose a valid option.")

        break

    else:
        count -= 1
        print("Incorrect PIN!")
        print(f"Attempts remaining: {count}")

else:
    print("Too many incorrect attempts.")
    print("Your account is locked.")
