#Creating a Database of Doctors and no.of patients visited 
#and filtering the doctors with more than 5 and Doctors with 0 patients

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rad297"
)

dr_db = mydb.cursor()

dr_db.execute("CREATE DATABASE Doctorss")

dr_db = mydb.cursor()

dr_db.execute("SHOW DATABASES")

for entry in dr_db:
  print(entry)

#OUTPUT
#('college',)
#('doctorss',)
#('information_schema',)
#('mydatabase',)
#('mysql',)
#('performance_schema',)
#('sakila',)
#('student_info',)
#('sys',)
#('world',)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Rad@97",
  database="Doctorss"
)
dr_db = mydb.cursor()

dr_db.execute("CREATE TABLE Doctors (dr_id VARCHAR(255), Patient_visited VARCHAR(255))")

dr_db = mydb.cursor()

sql = "INSERT INTO Doctors (dr_id , Patient_visited) VALUES (%s,%s)"
val = [
  ('Dr.Anu','7'),
    ('Dr.Ramya','2'),
    ('Dr.Gopal','6'),
    ('Dr.Vikas','1'),
    ('Dr.Rayudu','12'),
    ('Dr.Sam','19'),
    ('Dr.Vijay','10'),
    ('Dr.Joe','2'),
    ('Dr.Vinayak','0'),
    ('Dr.Riya','11'),
    ('Dr.Manoj','7'),
    ('Dr.Zoya','1'),
    ('Dr.Sha','9'), 
    ('Dr.Rio','4')
        
]

dr_db.executemany(sql, val)

mydb.commit()

print(dr_db.rowcount, "was inserted.")

#OUTPUT
#14 was inserted 

mycursor = mydb.cursor()

print("doctor(s) who have more than 5 patients visited : ")

mycursor.execute("SELECT * FROM Doctors where Patient_visited >5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#OUTPUT
#doctor(s) who have more than 5 patients visited : 
#('Dr.Anu', '7')
#('Dr.Gopal', '6')
#('Dr.Rayudu', '12')
#('Dr.Sam', '19')
#('Dr.Vijay', '10')
#('Dr.Riya', '11')
#('Dr.Manoj', '7')
#('Dr.Sha', '9')

mycursor = mydb.cursor()

print("doctor(s) who have 0 patients visited : ")

mycursor.execute("SELECT * FROM Doctors where Patient_visited=0")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#OUTPUT
#doctor(s) who have 0 patients visited : 
#('Dr.Vinayak', '0')
