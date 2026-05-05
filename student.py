class Student():
    name = "Hello"
    marks = [100,20]
    

    
    def grade(self):
        average = 0 
        for i in self.marks:
          average = average +i

        if average > 80:
            return "A grade"
        elif 79 <= average <= 60:
            return "B grade"
        
        elif 59<= average <=40:
            return "C grade"
        
        else:
            return "Fail"
        
    #def total(self):
       # return self.marks()
        
obj1 = Student()
print(obj1.name)
print(obj1.grade()) 
      
