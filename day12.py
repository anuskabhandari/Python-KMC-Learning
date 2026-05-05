class Math():

    def __init__(self , a, b, c):
        self.a = a
        self.b =b 
        self.c = c
        print(a,b,c)
    
    def add(self):
        return self.a+self.b+self.c

obj = Math(1,2,4)
print(obj.add())
