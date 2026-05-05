class Parent():
    a= "10"
    b= 100
    def add(self):
       return self.a + self.b

class Child(Parent):
    b = "HELLLOOO NAME"
    d =10
    def display(self):
       return self.add()

obj = Child()
#print(obj.display())  


class TestParent():
    def __init__(self):
        print("I am from Test Parent")

class TestChild(TestParent):
    def __init__(self):
        print("I am from test child")
        TestParent.__init__(self)
        super().__init__()

class Child(TestChild): 
    pass       

obj =Child(1,2,3)              