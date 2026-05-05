class StudentResult():
    def __init__(self, name, *marks):
        self.name = name
        self.marks =list(marks)

    def average(self):
        if len(self.marks) == 0:
            return"Zero Division Error", False
        
        return  sum(self.marks)/len(self.marks) , True
    
    def grade(self):
        
        if 80<self.average()<90:
            return "A grade"
        elif 70<self.average()<80:
            return "B grade"
        elif 60<self.average()<70:
            return "C grade"
        
        else:
            return "Fail"
        
    def display(self):
        return f"Average = {self.average()}\nGrade = {self.grade()}"
    
s = StudentResult("Helooo" , 1, 2, 59)
print(s.display())    

       
        
        
            

