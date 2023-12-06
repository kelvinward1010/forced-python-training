from bank_account import *

Kelvin = BankAccount(1000, "Kelvin")
Ward = BankAccount(2000, "Ward")


Kelvin.getBalance()
Ward.getBalance()

Kelvin.deopsit(999)

Kelvin.withdraw(10000666)

Kelvin.tranfer(10000, Ward)


Tyler = InterestAccount(1000, "Tyler")

Tyler.getBalance()
Tyler.deopsit(100)
Tyler.tranfer(100, Ward)

Locke = SavingAccount(1000, "Locke")

Locke.getBalance()
Locke.deopsit(100)
Locke.tranfer(100, Kelvin)