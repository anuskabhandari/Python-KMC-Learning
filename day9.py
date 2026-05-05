# keyword argument

def user_info(fname,lname,age):
    return f'my name is {fname} {lname} of {age}'
print(user_info("Heloo" , "Bhandari", "12"))
print(user_info(fname= "Helooo", age="22", lname="Bhandari"))

# arbitrary positional argument---> * thpera multiple value in arguments linxa and after using * it save in tuple

def sum_number(*num):
    print(num)
    print(type(num))

sum_number(1)
sum_number(1,2,3)

## summing
def sum_num(*num):
    sum= 0
    if len(num)>1:
        for i in num:
            sum +=i
        return f'Total sum {sum}'   
         
       
    else:
        return "This is not allowed in summing of the empty and a single number"
     

print(sum_num(1,2,3))     