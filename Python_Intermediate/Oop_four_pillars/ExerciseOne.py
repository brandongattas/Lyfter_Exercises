# 1. Cree una clase de BankAccount que:
#   -Tenga un atributo de balance.
#   -Tenga un método para ingresar dinero.
#   -Tengo un método para retirar dinero.
# Cree otra clase que herede de esta llamada SavingsAccount que:
#   -Tenga un atributo de min_balance que se pueda asignar al crearla.
#   -Arroje un error si al intentar retirar dinero, el retiro haría 
#    que el balance quede debajo del min_balance. Es decir que sí se 
#    pueden hacer retiros siempre y cuando el balance quede arriba del 
#    min_balance.

class BankAccount():
    def __init__(self):
        self.balance=0.0
        print(f"New bank account opened, current balance is ${self.balance}")

    def deposit_money(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount}, the current balance is: ${self.balance}")

    def withdraw_money(self, amount):
        self.balance -= amount
        print(f"Withdrawed: ${amount}, the current balance is: ${self.balance}")



class SavingsAccount(BankAccount):

    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance

    def withdraw_money(self, amount):
        print(f"Triying to withdraw ${amount}....")
        if (self.balance-amount) < self.min_balance:
            print(f"[ERROR] The balance is too low: ${self.balance}, the minimum balance must be: {self.min_balance} | withdrawal canceled.")
            return
        return super().withdraw_money(amount)

savings_account = SavingsAccount(500)
savings_account.deposit_money(600)
savings_account.withdraw_money(100)
savings_account.deposit_money(500)
savings_account.withdraw_money(600)
