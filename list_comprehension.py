## List comprehension--> print from 1 to 5
data = [1,2,3,4,5]
a=[i**2 for i in data]
print(a)
## for the even number
even = [i for i in data if i %2==0]

print(even)
#for the odd
odd = [ i for i in data if i%2!=0]
print(odd)


## taking the number from 1 to 10 ad addition of the 10 to each of them
data = [1,2,3,4,5,6,7,8,9,10]
add = [i+10 for i in data ]
print(add)