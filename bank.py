import json
import re
import sys
import time


class Bank:
    def __init__(self, balance=0, username="", password=""):
        self.balance = 0
        self.transactions = []
        self.credentials = {username: password} if username else {}
        self.grand_list = []
        self.current_user = None

    # --- PERSISTENCE ---
    def save(self, file_name, data):
        with open(file_name, "w") as file:
            json.dump(data, file, indent=4)

    def load(self, file_name):
        try:
            with open(file_name, "r") as file1:
                loaded_data = json.load(file1)
                self.grand_list = loaded_data
                return loaded_data
        except FileNotFoundError:
            self.grand_list = []
            return []

    # --- ACCOUNT OPERATIONS ---
    def deposit(self, amount):
        if not self.current_user:
            print("No active user session!")
            return

        if amount > 0:
            self.current_user["balance"] += amount
            self.current_user["transactions"].append(f"Deposited: {amount}")
            self.save("data.json", self.grand_list)
            print(f"Successfully deposited ${amount}")
        elif amount == 0:
            raise ValueError("Deposit amount cannot be zero.")
        else:
            raise ValueError("Deposit amount cannot be negative.")

    def withdraw(self, amount):
        if not self.current_user:
            print("No active user session!")
            return

        curr_balance = self.current_user["balance"]

        if amount > curr_balance:
            raise ValueError(
                f"Withdrawal exceeds balance! Current balance: {curr_balance}"
            )
        elif amount > curr_balance / 2:
            raise ValueError(
                "Withdrawal value is too high for a single transaction."
            )
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        else:
            self.current_user["balance"] -= amount
            self.current_user["transactions"].append(f"Withdrew: {amount}")
            self.save("data.json", self.grand_list)
            print(f"Successfully withdrew ${amount}")

    def show_balance(self):
        if self.current_user:
            print(
                f"\nYour current balance is: ${self.current_user['balance']}"
            )

    def history(self):
        if self.current_user:
            txs = self.current_user.get("transactions", [])
            if not txs:
                print("No transactions yet.")
            else:
                for item in txs:
                    print(item)

    def Exit(self):
        print("Goodbye!")
        sys.exit()

    # --- AUTHENTICATION ---
    def New_account(self):
        valid_username = r"^[a-zA-Z0-9_]{4,15}$"
        valid_password = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

        input_username = input(
            "Create Username (4-15 chars, letters/numbers/_ only): "
        ).strip()
        input_password = input(
            "Create Password (Min 8 chars, 1 Upper, 1 Lower, 1 Number, 1 Special): "
        )

        if re.match(valid_username, input_username) and re.match(
            valid_password, input_password
        ):
            account_data = {
                "username": input_username,
                "password": input_password,
                "balance": 0,
                "transactions": [],
            }
            self.grand_list.append(account_data)
            self.credentials[input_username] = input_password
            self.save("data.json", self.grand_list)

            print(f"Account for {input_username} created successfully!")
            self.current_user = account_data
            self.menu()
        else:
            raise ValueError("Weak password or invalid username")

    def login(self):
        user_input_u = input("Give your username: ").strip()
        user_input_p = input("Give your password: ")

        for account in self.grand_list:
            if (
                account["username"] == user_input_u
                and account["password"] == user_input_p
            ):
                print(f"Login successful! Welcome {user_input_u}")
                self.current_user = account
                self.menu()
                return

        print("Invalid username or password.")

    # --- DASHBOARD MENU ---
    def menu(self):
        while True:
            print("\n--- ACCOUNT DASHBOARD ---")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Transaction History")
            print("5. Logout")

            choice = input("Choose an option (1-5): ").strip()

            if choice == "1":
                self.show_balance()
            elif choice == "2":
                amt = float(input("Enter deposit amount: "))
                self.deposit(amt)
            elif choice == "3":
                amt = float(input("Enter withdrawal amount: "))
                self.withdraw(amt)
            elif choice == "4":
                self.history()
            elif choice == "5":
                self.current_user = None
                print("Logged out successfully.")
                break
            else:
                print("Invalid option.")


# --- MAIN PROGRAM EXECUTION ---
my_bank = Bank()
my_bank.load("data.json")

while True:
    print("\n--- WELCOME TO THE BANK ---")
    print("1. Create New Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Select an option (1-3): ").strip()

    if choice == "1":
        my_bank.New_account()
    elif choice == "2":
        my_bank.login()
    elif choice == "3":
        my_bank.Exit()
    else:
        print("Invalid choice, try again.")