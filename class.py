class Test():
    a = 567
    b = 400

    def add (self):
        return self.a + self.b
    

    def sub(self):
        return self.a - self.b
    
    
    def result(self):
        return self.add() , self.sub()
    
obj1 =  Test()
print(obj1.a)
print(obj1.add())    
print(obj1.result())