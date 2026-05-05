## day 17 ko continue
# JSon string
import json
person ={
    "name" : 'ram',
    "age" : 22,
    "address" : 'ktm',
    "skills" :['python' , 'django'],
     "is_programmer":True,
     "phone" : None}


person_json = json.dumps(person) # dictionary =>json
print(person_json, type(person_json))


"""
## json string => dictionary
import json
json_string ='''{
    "name" : "ram",
    "age" : 22,
    "address" : 'ktm',
    "skills" :['python' , 'django'],
     "is_programmer":true,
     "phone" : null}'''

x =    json.loads(json_string)
print(x, type(x))"""



# now opening the file
with open("person.json", "w") as f:
    f.write(person_json) # json string => json file

# Or we can do in the shotly
with open("person.json", "w") as f:
    json.dump(person,f,indent =4)   # dictionary to json fil---> dumps for the string and dump for the file okayyy
    # indent le chai space dekhaune garxa

with open("person.json", "r") as f:
    data = f.read()  # json => json string
    json_data = json.loads(data)  # json string => dictionary
    print(json_data, type(json_data))


 # mathi ko in one line ma garda--> gives the same output as above
with open("person.json", "r") as f:
    json_data = json.load(f) # json file to dictionary
    print(json_data , type(json_data))