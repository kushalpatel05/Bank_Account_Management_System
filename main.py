# Define a class to represent a bank user
class BankUser:
    bank_name = "State Bank of Python"  # Class attribute

    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.__balance = balance  # Instance attribute

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited to {self.name}'s account.")
        else:
            print("Invalid deposit amount.")\
            
    # Method to withdraw money 
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn from {self.name}'s account.")
        else:
            print("Insufficient balance or invalid amount.")

    # Method to get current balance
    def get_balance(self):
        return self.__balance

    # Static method to get bank name (does not access instance)
    @staticmethod
    def get_bank_name():
        return BankUser.bank_name

    # Class method to change the bank name
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # Display user information
    def show_info(self):
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Balance: ₹{self.__balance}")
        print(f"Bank: {BankUser.bank_name}")
        print("-" * 30)

# Input for user1
name1 = input("Enter your name: ")
email1 = input("Enter your email: ")
balance1 = float(input("Enter your initial balance: ₹"))
user1 = BankUser(name1, email1, balance1)

# Input for user2
name2 = input("\nEnter second user's name: ")
email2 = input("Enter second user's email: ")
balance2 = float(input("Enter second user's initial balance: ₹"))
user2 = BankUser(name2, email2, balance2)

# Show initial information
print("\nAccount Information:")
user1.show_info()
user2.show_info()

# Transactions
for user in [user1, user2]:
    print(f"\nTransaction for {user.name}")
    action = input("Type 'd' to Deposit or 'w' to Withdraw: ").lower()
    amount = float(input("Enter the amount: ₹"))

    if action == 'd':
        user.deposit(amount)
    elif action == 'w':
        user.withdraw(amount)
    else:
        print("Invalid action selected.")

# Ask if user wants to change bank name 
print("\nCurrent Bank:", BankUser.get_bank_name())
choice = input("Do you want to change the bank name? (yes/no): ").lower()

if choice == 'yes':
    new_bank = input("Enter the new bank name: ")
    BankUser.change_bank_name(new_bank)
    print("✅ Bank name updated.")
else:
    print("✅ Bank name remains unchanged.")

# Show updated balances
print("\nFinal Account Balances:")
print(f"{user1.name}'s Balance:", user1.get_balance())
print(f"{user2.name}'s Balance:", user2.get_balance())
print("-"*30)

# Show updated info
print("Updated Account Information:")
user1.show_info()
user2.show_info()