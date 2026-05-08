"""import mysql.connector
db = mysql.connector.connect(
    host = "localhost",
    username = "root",
)
print(db)
"""

import sqlite3
connection = sqlite3.connect('students.sqlite3')

terminal = connection.cursor()

# insert query
query = 'Insert into student(id,name,address,college,age,gender,faculty,university) values (12 , "test", "address", "college" , 15 , "m" ,"tu", "tu")'

terminal.execute(query)
connection.commit()
print(connection)



# delete query
query = "DELETE FROM student WHERE id = 10"

terminal.execute(query)
connection.commit()

print("Deleted successfully")   

# update query
query = "UPDATE student SET name = 'Ram' WHERE id = 10"

terminal.execute(query)
connection.commit()

print("Updated successfully")

# read query
query = 'select id,name , faculty , university from student'
terminal.execute(query)
result = terminal.fetchall()
print(result)

for i in result:
    print(i)