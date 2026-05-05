class Rectangle():
    def __init__(self,l,b):
        self.l =l
        self.b = b
        print(l,b)

    def area(self):
        return self.l *self.b    
obj = Rectangle(10,12)
print(obj.area())

## deault value use---> employee
class Employee():
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        print(name, salary)
    def details(self):
        return self.name , self. salary
            
e = Employee("helooooo" , 30000)  
print(e.details())
