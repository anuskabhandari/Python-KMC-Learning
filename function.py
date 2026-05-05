def test():
    a = 100
    print("The value of a is",a)
    return [1,2,4,5,6,7,8],[8,9]

print(test())

## function bhitra print lekhna mildaina and also input nii
## if using the loop dont use the return tyo le program complte garna didaina
# eutai function ma duita duita datatype napathau vnca
def sum_of_list():
    a = [1,2,3,4,5,6]
    total = 0
    for i in a:
        total += i
    return total
    
print(sum_of_list())  


def check_number(num):
    if num%2 == 0:
        return "even"
    
    else:
        return "odd"
result = check_number(10)
print(result)


def max_list():
    a = [2,3,45,67,899,0]
    max = a[0]
    for i in a: 
        if i > max:
           max = i
        
    return max
        
print(max_list())        




