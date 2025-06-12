class ATM:
    def __init__(self, pin):
        self.balance = 0.0
        self.pin = pin
        self.transactions = []

    def verify_pin(self):
        pin = int(input("Enter PIN: "))
        if pin == self.pin:
            return True
        else:
            print("Incorrect PIN")
            return False

    def check_balance(self):
        print(f"Your current balance is: {self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully. Balance: {self.balance}")
            self.transactions.append(f"Deposited {amount}")
        else:
            print("Enter a valid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn amount: {amount}. Balance: {self.balance}")
            self.transactions.append(f"Withdrawn {amount}")
        else:
            print("Insufficient balance")

    def change_pin(self):
        old_pin = int(input("Enter old PIN: "))
        if old_pin == self.pin:
            new_pin = int(input("Enter new PIN: "))
            confirm_pin = int(input("Confirm new PIN: "))
            if new_pin == confirm_pin and len(str(new_pin)) == 4:
                self.pin = new_pin
                print("PIN changed successfully")
                self.transactions.append("PIN changed")
            else:
                print("PIN didn't match")
        else:
            print("Incorrect old PIN")

    def transaction_history(self):
        if self.transactions:
            print("Transaction History:")
            for trans in self.transactions:
                print(trans)
        else:
            print("No transactions found")


# Make sure the main() function is outside the class
def main():
    pin = int(input("Enter your 4-digit PIN: "))
    account = ATM(pin)
    if not account.verify_pin():
        print("Access denied")
        return

    while True:
        print("\n--- ATM MENU ---")
        print("1. Balance Enquiry")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            account.check_balance()
        elif choice == 2:
            account.withdraw(float(input("Enter amount: ")))
        elif choice == 3:
            account.deposit(float(input("Enter amount: ")))
        elif choice == 4:
            account.change_pin()
        elif choice == 5:
            account.transaction_history()
        elif choice == 6:
            print("Thank you for visiting!")
            break
        else:
            print("Enter a valid choice")


# This must also be outside the class and not indented
if __name__ == "__main__":
    main()

