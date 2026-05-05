# For loop
for i in [1,2,3,4,5,1]:
   print(i)
   print("kmc")

for i in [12, 13 ,15,16]:
   if (i%2==0):
     print(f'{i} is even')   

# dictionary
a ={
   "name " : "hari",
   "college" : "kmc"
}

for i in a:
   print(f'{i} = "{a[i]}"')

#for i in a.values:
   #print(i)

#range practice
for i in range(1,10,1):
   print(i)

#odd even in range
odd =[]
even=[i]
for i in range(10,20):
  
  if i %2==0:
     
     even.append(i)
  else:
      odd.append(i)
print(even)  

# Removing the string data
for i in[1,2,3,4,"hello","test", 1,2,3,4]:
   if isinstance(i,int): # USING type(i) is not a nice approach
      print(i)
   

# Addition
a= [10,20,30,40]
sum =0
for i in a:
   sum = sum+i
   print(sum)

# i ,j
for i in [1,2,3]:
   for j in [4,5,6,7]:
      print(i,j) 

# While loop--> infinite loop
# for loop -->finite loop
i = 1
while(i<=10):
 
  print(i)
  i = i+ 1


# List display
a= [1,2,3,4,5,6,7,7,"hello","test"]
while(a):
   print (a)
   break


        

   