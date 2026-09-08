import sys
import re
import time

class Bank:  # Capitalized class name following PEP 8 guidelines
    def __init__(self, balance, username, password):
        # Removed self.amount since transactions handle their own amounts
        self.balance = balance
        self.transactions = []
        self.credentials = {username: password}

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited: {amount}")
        elif amount == 0:
            raise ValueError("Deposit amount cannot be zero.")
        else:
            raise ValueError("Deposit amount cannot be negative.")
        

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError(f"The withdrawal amount is more than your current balance, which is {self.balance}")
        elif amount > self.balance / 2:
            raise ValueError("Withdrawal value is too high for a single transaction.")
        elif amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            self.transactions.append(f"withdrawed: {amount}")


    def show_balance(self):  # Lowercase method name following PEP 8
        print(f"Your current balance is {self.balance} dollars.")

    def history(self):
        if not self.transactions:
            print("wrpng")
        for item in self.transactions:
            print(item)

    def Exit(self):
        sys.exit()

    def New_account(self):
        valid_username = r"^[a-zA-Z0-9_]{4,15}$"
        valid_password =  r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
        username = input("Create Username (4-15 chars, letters/numbers/_ only): ").strip()
        password = input("Create Password (Min 8 chars, 1 Upper, 1 Lower, 1 Number, 1 Special: 3637: ")

        if re.match(valid_username, username) and re.match(valid_password, password):
            self.credentials[username] = password
            self.menu()
        else:
            raise ValueError("weak password or invalid username")

    def login(self):
        user_input_u = input("give your username: ")
        user_input_p = input("give your password: ")

        if user_input_u in self.credentials and self.credentials[user_input_u] == user_input_p:
            print("Login successful!")
            self.menu()
        else:
            print("Invalid username or password.")
    def menu(self):
        while True:
            print("\n--- ACCOUNT DASHBOARD ---")
            print("1. Show Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. View Transaction History")
            print("5. Exit")
            
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
                self.Exit()
            else:
                print("Invalid option.")

# Create one bank object instance
my_bank = Bank(balance=0, username="", password="")

# Phase 1: Startup / Authentication Loop
while True:
    print("\n--- WELCOME TO THE BANK ---")
    print("1. Create New Account")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Select an option (1-3): ").strip()
    
    if choice == "1":
        my_bank.New_account()
        break  # Move to the main account menu after creation
    elif choice == "2":
        my_bank.login()
        break  # Move to the main account menu after successful login
    elif choice == "3":
        my_bank.Exit()
    else:
        print("Invalid choice, try again.")