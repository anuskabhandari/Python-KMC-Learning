"""f = open("hello.txt","w")
f.write("Hello World")
f.close()

f= open("hello.txt", "r")
print(f.read())
f.close()


print("Hello")
1/0
print("Hiii")

f= open("hello.txt", "r")
print(f.read())
1/0
f.close()"""

## error handling in file handling
try: 
    f= open("hello.txt", "r")
    print(f.read())
    1/0
    f.close()

except ZeroDivisionError:
    print("cannot be divide by 0")  
f.closed
