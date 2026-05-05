with open("sample_users.csv", "r") as f:
    print(f.read())

# csv --> comma separated values
import csv
with open("sample_users.csv", "r") as f:
    data = csv.reader(f)
    for i in data:
       # print(i) 
       print (i[0], i[3])
with open("sample_users.csv", "r") as f:
    data = csv.DictReader(f)
    for i in data:
        print(i['first_name'], i['address'])   
