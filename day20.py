class A():
    __a = 1
    b = __a +1 # __ this is used for the private

    def __add(self):
        return self.__a + self.b
    
    def public_add(self):
        return self.__add()
    
obj = A()
print(obj.b)
#print(__add())

class BankAccount():
    accountholder = "----"
    __balance = 1000


    def withdraw(self,amount):
        self.__balance -= amount
        return "success"
    
    def deposit(self,amount):
        self.balance += amount
        return amount
    
    
    def showBalance(self):
        return self.__balance

class StudentAccount(BankAccount) :
    studentId = 1
    
    def PayLibraryFine(self,amount): # yesma directly balance access garna paudaina because tyo arko class ko private hoo
        return self.withdraw(amount) 


obj = StudentAccount()
print(obj.PayLibraryFine(100))
print(obj.showBalance())
    
