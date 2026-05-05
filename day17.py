# with open le file open vaye paxi automatically close pani garxa
"""
with open("hello.txt", "w") as f:
    f.write("Hello World")
print(f.closed)  """

with open("hello.txt", "r") as f:
    print(f.closed)# file bhitrai close garda false aauxa
    print(f.read()) 
print(f.closed)

with open("hello.txt", "r") as f:
    print(f.read(10))
    print(f.tell())



with open("hello.txt", "r") as f:
    print(f.read(10))  # read  first 10 charcter
    print(f.tell())
    f.seek(0)   # 0 position ko lai khojxa ttesma
    print(f.tell())


# readline --> print(f.readline())

# wiwth loop-->
with open("hello.txt","r") as f:
    for i in f:
        print(i)

with open("showcase.png", "r") as f: 
    print(f.read())       