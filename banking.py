class Account():
    acc_number = int(input("Enter account number: "))
    balance = int(input("Enter balance: "))

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance = self.balance - amount
        return self.balance


class SavingAccount(Account):
    interest_rate = int(input("Enter interest rate: "))

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance = self.balance + interest
        return self.balance
    
obj = SavingAccount()

obj.deposit(500)
print("After deposit:", obj.balance)

obj.withdraw(200)
print("After withdraw:", obj.balance)

obj.add_interest()
print("After interest:", obj.balance)    
