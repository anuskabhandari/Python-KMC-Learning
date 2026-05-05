import csv
"""
student = ('Ramesh', 'ktm',22) # yo tuple lai read garne aaba
with open('student.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(student) # single write at once

## Multiple value wala
students=[
    ("Name" , "Address", "Age"),
    ('Ram' , 'ktm' , 23),
    ('Rekha' , 'kritipur' , 22),
     ('hello' , 'ktm' , 23),
    ('Misss' , 'ktm' , 23)

]  
with open('students.csv', 'w') as f:
    writer = csv.writer(f)
    for student in students:
        writer.writerow(student)
## writerows le chai bulk file write or the multiple files written at once

# writing the dictionary now
students = {'name': "Ram", "address": "ktm", "age":23}  # Dictionary writer// difference between dict writer and writer
with open('person.csv', 'w') as f:
    writer = csv.DictWriter(f,  fieldnames = students.keys())
    writer.writeheader()
    for student in students:
        writer.writerow(student) 


# multiple files in dictionary
students = [
    {'name': "Ram", "address": "ktm", "age":23},
    {'name': "Rekha", "address": "ktm", "age":22},
    {'name': "Sita", "address": "ktm", "age":20},
    {'name': "Anuska", "address": "ktm", "age":19},
]        

with open('person.csv', 'w') as f:
    writer = csv.DictWriter(f,  fieldnames = ['name' , 'address','age'])
    writer.writeheader()
    for student in students:
        writer.writerow(student) 

        # when using writer.writerows(students)--> then it will bulk write at once

"""
import os
try:
   os.remove("person.csv")

except FileNotFoundError:
    print("File  does not exist.")

print(os.path.exists("student.csv") )   # file xa ki xaina check garxa--> if exits true else false


if os.path.exists("student.csv")  :
    os.remove("student.csv")
else:
    print("File does not exists.")

#os.mkdir("hello") # make directory / folder
#os.rename("hello", "hi")  
#os.rmdir("hi") # remove directory


# Do task
ls= [1,2,4,5,6,7]
output = []
for i in ls:
    output.append(i **2)
print(output)


output = [ i**2 for i in ls]
print(output)


## comprehension for the if condition
age =17
# ternary operator
is_authorized = "Unauthorized" if age < 18 else "Authorized"
print(is_authorized)
"""
#Odd even  for each
numbers = [1,2,3,4,5]
output = []
for i in numbers:
    if i % 2==0:
        output.append('EVEN')
    else:
        output.append('ODD')  
print(output)          
"""
# using the ternary
numbers = [1,2,3,4,5]
output=['even' if i %2==0 else 'odd' for i in numbers]
print(output)

# Positive numbers
numbers = [ -8 , -7,3,-1, 0,1,3,4,5,-7,6,8,10]
output = [ 'positive ' if i>0 else 'negative' for i in numbers]
print(output)

numbers = [ -8 , -7,3,-1, 0,1,3,4,5,-7,6,8,10]
output =[i for i in numbers if i>0]
print(output)


# now dictionary comprehension-->yesma chahi update use hunxa
# items is used to get the both values and keys
us_price = {'milk' : 2.05, 'bread' : 2.6, 'butter':2.6}
nep_price={}

for k,v in  us_price.items():
    nep_price.update({k : v*145})
print(nep_price)    


# Pythonic way =>dictionary comprehension
us_price = {'milk' : 2.05, 'bread' : 2.6, 'butter':2.6}

nep_price = {
    k:v *145
    for k,v in us_price.items()
}
print(nep_price)
