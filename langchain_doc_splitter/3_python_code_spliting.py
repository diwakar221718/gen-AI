#document splitting
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text="""
class ATM:
    def __init__(self, account_holder, pin, balance=0):
        self.account_holder = account_holder
        self.__pin = pin          # Private attribute
        self.__balance = balance  # Private attribute

    def check_pin(self, pin):
        return self.__pin == pin

    def check_balance(self):
        print(f"Current Balance: ₹{self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
            self.check_balance()
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            self.check_balance()


# ---------------- MAIN PROGRAM ----------------

name = input("Enter Account Holder Name: ")
pin = input("Set a 4-digit PIN: ")
balance = float(input("Enter Initial Balance: ₹"))

atm = ATM(name, pin, balance)

entered_pin = input("\nEnter PIN to access ATM: ")

if atm.check_pin(entered_pin):

    while True:
        print("\n====== ATM MENU ======")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            atm.deposit(amount)

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            atm.withdraw(amount)

        elif choice == "4":
            print("Thank you for using the ATM!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access Denied.")
    
    """

#initialize splitter
splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0
)

# perform split
chunk=splitter.split_text(text)

print(len(chunk))
print(chunk[0])