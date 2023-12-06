class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, initialName):
        self.initialAmount = initialAmount
        self.initialName = initialName
        print(f"\nAccount '{self.initialName}' created.\nBalance = ${self.initialAmount:.2f}")

    def getBalance(self):
        print(f"\nAccount '{self.initialName}' balance = ${self.initialAmount:.2f}")
        
    def deopsit(self, amount):
        self.balance = self.initialAmount + amount
        print(f"\nAccount '{self.initialName}' have desopsit = ${self.balance}")
        self.getBalance()
        
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            BalanceException(f"\nSorry, acoount '{self.initialName}' only has a balance {self.balance}")
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWith draw complete.")
            self.getBalance()
        except BalanceException as error:
            print("\nError something! {error}")
            
    def tranfer(self, amount, account):
        try:
            print("\n*****\n\nBegginning tranfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deopsit(amount)
            print('\nDone tranfer! ************')
        except BalanceException as error:
            print("\nError something! {error}")


class InterestAccount(BankAccount):
    def deopsit(self, amount):
        #self.balance = self.balance + (amount * 1.05)
        print("\nDesopsit complete.")
        self.getBalance()
        
class SavingAccount(InterestAccount):
    def __init__(self, initialAmount, initialName):
        super().__init__(initialAmount, initialName)
        self.fee = 5
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount = self.fee)
            self.balance = self.balance + (amount + self.fee)
            print("\nSaving transaction complete")
            self.getBalance()
        except BalanceException as error:
            print("\nError something! {error}")   
        