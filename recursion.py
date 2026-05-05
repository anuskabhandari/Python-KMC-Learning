# recursion---> function calling iteself
def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)
    
print(fact(5))    

## class and objects---> class is the house and object is the map
# under the class function become the method and variable become attributes


