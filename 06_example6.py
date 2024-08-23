class BankAccount:
    def __init__(self, account_holder, balance = 0):
        self.account_holder = account_holder
        self.__balance = balance # private attribute can be accessed from outside the calss
    def deposite(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposite {amount}. Total balance is {self.__balance}")
    def withdraw(self, amount):
        if 0 < amount < self.__balance:
            self.__balance -= amount
            print(f"Withdraw amount {amount}. Remaining Balance {self.__balance}")
        else:
            print("Insufficient Balance")
    def get_info(self):
        return self.__balance # method to access the balance attribute

my_bank_account = BankAccount("Raiyan", 1000)
my_bank_account.deposite(200)
my_bank_account.withdraw(100)
print(my_bank_account.get_info())

my_bank_account.deposite(50000)
print(my_bank_account.get_info())