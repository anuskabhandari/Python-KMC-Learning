class Parent1():
    a = 10
    b= 11

class Parent2():
    c = 100
    d= 10

class Child(Parent1, Parent2):
    a =2


obj = Child()
print(obj.a)
print(Child.__mro__)


## lambda function
#--> normal function using
def add(x,y):
    return x+y

print(add(1,2))

# using
data = lambda x,y :x+y
print(data(1,2))

data = [1,2,3,4]
a = [i**2 for i in data]
print(a)


# Lambda function to get the square of multiple data

square = lambda **args : [i**2 for i in args]

print(square(1,2,3,4,5))
print(square(15,26))