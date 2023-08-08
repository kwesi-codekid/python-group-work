from atm import ATM


class ATMMain:
    def __init__(self):
        self.atm = ATM()

    def validate_input(self, input_text, input_type):
        while True:
            try:
                value = int(input(input_text))
                return value
            except ValueError:
                print(f"Invalid input. Please enter a valid {input_type}.")

    def main_menu(self):
        while True:
            print("ATM Menu:")
            print("1. Create Account")
            print("2. Login")
            print("3. Check Balance")
            print("4. Withdraw")
            print("5. Deposit")
            print("6. Exit")

            try:
                choice = input("Select an option: ")

                if choice == "1":
                    account_number = self.validate_input(
                        "Enter account number: ", 'number')
                    pin = self.validate_input("Enter PIN: ", 'PIN')
                    initial_balance = float(input("Enter initial balance: "))
                    if self.atm.create_account(account_number, pin, initial_balance):
                        print("Account created successfully.")
                    else:
                        print("Account creation failed. Account already exists.")

                elif choice == "2":
                    account_number = input("Enter account number: ")
                    pin = input("Enter PIN: ")
                    account = self.atm.login(account_number, pin)
                    if account:
                        print("Logged in successfully.")
                        while True:
                            print("1. Check Balance")
                            print("2. Withdraw")
                            print("3. Deposit")
                            print("4. Logout")
                            sub_choice = input("Select an option: ")

                            if sub_choice == "1":
                                balance = self.atm.check_balance(
                                    account_number)
                                if balance is not None:
                                    print(f"Current balance: ${balance:.2f}")
                                else:
                                    print("Account not found.")
                            elif sub_choice == "2":
                                try:
                                    amount = float(
                                        input("Enter amount to withdraw: "))
                                    new_balance = self.atm.withdraw(
                                        account_number, amount)
                                    if new_balance is not None:
                                        print(
                                            f"Withdrawal successful. New balance: ${new_balance:.2f}")
                                    else:
                                        print("Insufficient funds.")
                                except ValueError:
                                    print(
                                        "Invalid input. Please enter a valid amount.")
                            elif sub_choice == "3":
                                try:
                                    amount = float(
                                        input("Enter amount to deposit: "))
                                    new_balance = self.atm.deposit(
                                        account_number, amount)
                                    if new_balance is not None:
                                        print(
                                            f"Deposit successful. New balance: ${new_balance:.2f}")
                                    else:
                                        print("Deposit failed.")
                                except ValueError:
                                    print(
                                        "Invalid input. Please enter a valid amount.")
                            elif sub_choice == "4":
                                break
                            else:
                                print("Invalid option.")
                    else:
                        print("Login failed.")

                elif choice == "3":
                    account_number = input("Enter account number: ")
                    balance = self.atm.check_balance(account_number)
                    if balance is not None:
                        print(f"Current balance: ${balance:.2f}")
                    else:
                        print("Account not found.")

                elif choice == "4":
                    try:
                        account_number = input("Enter account number: ")
                        amount = float(input("Enter amount to withdraw: "))
                        new_balance = self.atm.withdraw(account_number, amount)
                        if new_balance is not None:
                            print(
                                f"Withdrawal successful. New balance: ${new_balance:.2f}")
                        else:
                            print("Insufficient funds or account not found.")
                    except ValueError:
                        print("Invalid input. Please enter a valid amount.")

                elif choice == "5":
                    try:
                        account_number = input("Enter account number: ")
                        amount = float(input("Enter amount to deposit: "))
                        new_balance = self.atm.deposit(account_number, amount)
                        if new_balance is not None:
                            print(
                                f"Deposit successful. New balance: ${new_balance:.2f}")
                        else:
                            print("Account not found.")
                    except ValueError:
                        print("Invalid input. Please enter a valid amount.")

                elif choice == "6":
                    self.atm.close()
                    print("ATM closed. Goodbye!")
                    break

                else:
                    print("Invalid option.")
            except KeyboardInterrupt:
                print("Program terminated by user.")
                break
            except Exception as e:
                print(f"An error occurred: {e}")


if __name__ == "__main__":
    atm_main = ATMMain()
    atm_main.main_menu()
